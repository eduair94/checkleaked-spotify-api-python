/**
 * Generate the Python resource surface from the canonical TypeScript SDK.
 *
 * The TypeScript resource classes own the public namespace/method names and
 * parameter optionality. The checked-in OpenAPI snapshot owns wire paths and
 * parameter locations. The generated Python methods use snake_case and retain
 * camelCase aliases for exact npm parity.
 */

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createRequire } from 'node:module';

const scriptDir = path.dirname(fileURLToPath(import.meta.url));
const packageRoot = path.resolve(scriptDir, '..');
const tsPackageRoot = path.resolve(packageRoot, '..', 'spotify-api-sdk');
const require = createRequire(import.meta.url);
const ts = require(path.join(tsPackageRoot, 'node_modules', 'typescript'));

const resourcesDir = path.join(tsPackageRoot, 'src', 'resources');
const openApiPath = path.join(tsPackageRoot, 'openapi.json');
const outputPath = path.join(
  packageRoot,
  'src',
  'spotify_api_sdk',
  'resources.py',
);
const referencePath = path.join(packageRoot, 'API_REFERENCE.md');
const spec = JSON.parse(fs.readFileSync(openApiPath, 'utf8'));

const PYTHON_KEYWORDS = new Set([
  'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
  'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
  'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
  'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield',
]);

function snakeCase(value) {
  const snake = value
    .replace(/([a-z0-9])([A-Z])/g, '$1_$2')
    .replace(/([A-Z]+)([A-Z][a-z])/g, '$1_$2')
    .replace(/-/g, '_')
    .toLowerCase();
  return PYTHON_KEYWORDS.has(snake) ? `${snake}_` : snake;
}

function normalizePath(value) {
  return value.replace(/\{[^}]+\}/g, '{}');
}

function findInitializer(name, body) {
  let found;
  function walk(node) {
    if (
      ts.isVariableDeclaration(node)
      && ts.isIdentifier(node.name)
      && node.name.text === name
      && node.initializer
    ) {
      found = node.initializer;
    }
    ts.forEachChild(node, walk);
  }
  walk(body);
  return found;
}

function resolvePath(expression, sourceFile, body) {
  if (ts.isIdentifier(expression)) {
    const initializer = findInitializer(expression.text, body);
    if (initializer) return resolvePath(initializer, sourceFile, body);
  }
  if (ts.isStringLiteralLike(expression)) return expression.text;
  if (
    ts.isCallExpression(expression)
    && ts.isIdentifier(expression.expression)
    && expression.expression.text === 'buildPath'
  ) {
    return resolvePath(expression.arguments[0], sourceFile, body);
  }
  if (ts.isTemplateExpression(expression)) {
    let result = expression.head.text;
    for (const span of expression.templateSpans) {
      const match = span.expression
        .getText(sourceFile)
        .match(/params\.([A-Za-z_$][\w$]*)/);
      if (!match) {
        throw new Error(
          `Cannot resolve template path expression: ${span.expression.getText(sourceFile)}`,
        );
      }
      result += `{${match[1]}}${span.literal.text}`;
    }
    return result;
  }
  throw new Error(`Unsupported path expression: ${expression.getText(sourceFile)}`);
}

function resolveParameter(parameter) {
  if (!parameter?.$ref) return parameter;
  const name = parameter.$ref.split('/').at(-1);
  return spec.components?.parameters?.[name] ?? parameter;
}

function schemaFor(operation, location, name) {
  if (location === 'body') {
    return operation.requestBody?.content?.['application/json']?.schema
      ?.properties?.[name];
  }
  return (operation.parameters ?? [])
    .map(resolveParameter)
    .find((parameter) => parameter?.in === location && parameter.name === name)
    ?.schema;
}

function annotation(typeText, schema) {
  if (typeText.includes('IdList')) return 'IdList';
  if (typeText.endsWith('[]') || schema?.type === 'array') {
    const itemType = schema?.items?.type === 'integer' ? 'int' : 'str';
    return `Sequence[${itemType}]`;
  }
  if (schema?.type === 'integer') return 'int';
  if (schema?.type === 'number') return 'float';
  if (schema?.type === 'boolean' || typeText === 'boolean') return 'bool';
  if (
    schema?.type === 'string'
    || typeText === 'string'
    || /^'.*'(?:\s*\|\s*'.*')+$/.test(typeText)
  ) {
    return 'str';
  }
  if (typeText === 'number') return 'int';
  return 'Any';
}

function interfaceProperties(interfaceNode, sourceFile) {
  return interfaceNode.members
    .filter(ts.isPropertySignature)
    .map((member) => ({
      wireName: member.name.getText(sourceFile).replace(/^['"]|['"]$/g, ''),
      typeText: member.type?.getText(sourceFile) ?? 'unknown',
      required: !member.questionToken,
    }));
}

function findClientCall(method) {
  let found;
  function walk(node) {
    if (
      ts.isCallExpression(node)
      && ts.isPropertyAccessExpression(node.expression)
      && ts.isPropertyAccessExpression(node.expression.expression)
      && node.expression.expression.expression.kind === ts.SyntaxKind.ThisKeyword
      && node.expression.expression.name.text === 'client'
      && ['get', 'post', 'delete'].includes(node.expression.name.text)
    ) {
      found = node;
    }
    ts.forEachChild(node, walk);
  }
  walk(method.body);
  return found;
}

function parseResource(fileName) {
  const absolutePath = path.join(resourcesDir, fileName);
  const source = fs.readFileSync(absolutePath, 'utf8');
  const sourceFile = ts.createSourceFile(
    fileName,
    source,
    ts.ScriptTarget.Latest,
    true,
  );
  const interfaces = new Map();
  let resourceClass;

  sourceFile.forEachChild((node) => {
    if (ts.isInterfaceDeclaration(node)) interfaces.set(node.name.text, node);
    if (
      ts.isClassDeclaration(node)
      && node.name?.text.endsWith('Resource')
    ) {
      resourceClass = node;
    }
  });
  if (!resourceClass) throw new Error(`No resource class in ${fileName}`);

  const namespace = fileName.replace(/\.ts$/, '');
  const methods = [];
  for (const method of resourceClass.members.filter(ts.isMethodDeclaration)) {
    if (!method.name || !method.body) continue;
    const clientCall = findClientCall(method);
    if (!clientCall) {
      throw new Error(`${fileName}:${method.name.getText(sourceFile)} has no client call`);
    }
    const verb = clientCall.expression.name.text;
    const sourcePath = resolvePath(
      clientCall.arguments[0],
      sourceFile,
      method.body,
    );
    const candidates = Object.keys(spec.paths).filter(
      (candidate) => normalizePath(candidate) === normalizePath(sourcePath),
    );
    if (candidates.length !== 1) {
      throw new Error(
        `${fileName}:${method.name.getText(sourceFile)} path ${sourcePath} `
        + `matched ${candidates.length} OpenAPI paths`,
      );
    }
    const wirePath = candidates[0];
    const operation = spec.paths[wirePath][verb];
    if (!operation) {
      throw new Error(`${fileName}: missing ${verb.toUpperCase()} ${wirePath}`);
    }

    const parameters = [...method.parameters];
    const first = parameters[0];
    let fields = [];
    let genericBody = false;
    let genericQuery = false;
    if (first) {
      const firstName = first.name.getText(sourceFile);
      const firstType = first.type?.getText(sourceFile) ?? 'unknown';
      if (firstName === 'params' && interfaces.has(firstType)) {
        fields = interfaceProperties(interfaces.get(firstType), sourceFile);
      } else if (firstName === 'body') {
        genericBody = true;
      } else if (firstName === 'query') {
        genericQuery = true;
      }
    }
    if (parameters.some((parameter) => parameter.name.getText(sourceFile) === 'body')) {
      genericBody = true;
    }
    if (parameters.some((parameter) => parameter.name.getText(sourceFile) === 'query')) {
      genericQuery = true;
    }

    const pathNames = new Set(
      [...wirePath.matchAll(/\{([^}]+)\}/g)].map((match) => match[1]),
    );
    const bodyNames = new Set(
      Object.keys(
        operation.requestBody?.content?.['application/json']?.schema
          ?.properties ?? {},
      ),
    );
    const mappedFields = fields.map((field) => {
      const location = pathNames.has(field.wireName)
        ? 'path'
        : bodyNames.has(field.wireName)
          ? 'body'
          : 'query';
      return {
        ...field,
        pythonName: snakeCase(field.wireName),
        location,
        annotation: field.wireName === 'ids'
          ? 'IdList'
          : annotation(
              field.typeText,
              schemaFor(operation, location, field.wireName),
            ),
      };
    });

    methods.push({
      namespace,
      className: resourceClass.name.text,
      tsName: method.name.getText(sourceFile),
      pythonName: snakeCase(method.name.getText(sourceFile)),
      verb: verb.toUpperCase(),
      path: wirePath,
      fields: mappedFields,
      genericBody,
      genericQuery,
    });
  }
  return {
    namespace,
    className: resourceClass.name.text,
    methods,
  };
}

const resources = fs.readdirSync(resourcesDir)
  .filter((fileName) => fileName.endsWith('.ts') && fileName !== 'base.ts')
  .sort()
  .map(parseResource);

const methods = resources.flatMap((resource) => resource.methods);
if (resources.length !== 25 || methods.length !== 110) {
  throw new Error(
    `Expected 25 namespaces / 110 methods, got ${resources.length} / ${methods.length}`,
  );
}

function pyTuple(pairs) {
  if (pairs.length === 0) return '()';
  const items = pairs
    .map(([pythonName, wireName]) => `(${JSON.stringify(pythonName)}, ${JSON.stringify(wireName)})`)
    .join(', ');
  return pairs.length === 1 ? `(${items},)` : `(${items})`;
}

function optionalAnnotation(type) {
  return type === 'Any' ? 'Any' : `Optional[${type}]`;
}

function methodSource(method) {
  const required = method.fields.filter((field) => field.required);
  const optional = method.fields.filter((field) => !field.required);
  const positional = required.map(
    (field) => `${field.pythonName}: ${field.annotation}`,
  );
  if (method.genericBody) positional.push('body: Any = None');
  else if (method.genericQuery) positional.push('query: Optional[QueryParams] = None');

  const keyword = optional.map(
    (field) => `${field.pythonName}: ${optionalAnnotation(field.annotation)} = None`,
  );
  if (method.genericBody && method.genericQuery) {
    keyword.push('query: Optional[QueryParams] = None');
  }
  if (!method.genericQuery) {
    keyword.push('extra_query: Optional[QueryParams] = None');
  }
  if (method.verb === 'POST' && !method.genericBody) {
    keyword.push('body: Optional[Mapping[str, Any]] = None');
  }
  keyword.push(
    'request_timeout: Optional[float] = None',
    'request_retries: Optional[int] = None',
    'request_headers: Optional[Headers] = None',
  );

  const signature = positional.length > 0
    ? [...positional, '*', ...keyword]
    : ['*', ...keyword];
  const endpointName = `_${method.namespace.toUpperCase()}_${snakeCase(method.tsName).toUpperCase()}`;
  const lines = [
    `    def ${method.pythonName}(`,
    '        self,',
    ...signature.map((part) => `        ${part},`),
    '    ) -> Any:',
    `        """${method.verb} ${method.path}."""`,
    `        return self._invoke(${endpointName}, locals())`,
  ];
  if (method.tsName !== method.pythonName) {
    lines.push('', `    ${method.tsName} = ${method.pythonName}`);
  }
  return lines.join('\n');
}

const generated = [
  '"""Generated Spotify Data API resource namespaces.',
  '',
  'Do not edit manually. Run ``node scripts/generate_resources.mjs``.',
  '"""',
  '',
  'from __future__ import annotations',
  '',
  'from typing import Any, Dict, Mapping, Optional, Sequence, Type',
  '',
  'from ._resource import Endpoint, Resource',
  'from .types import Headers, IdList, QueryParams',
  '',
  `ENDPOINT_COUNT = ${methods.length}`,
  `NAMESPACE_COUNT = ${resources.length}`,
  '',
];

for (const method of methods) {
  const endpointName = `_${method.namespace.toUpperCase()}_${snakeCase(method.tsName).toUpperCase()}`;
  const pathFields = method.fields
    .filter((field) => field.location === 'path')
    .map((field) => [field.pythonName, field.wireName]);
  const queryFields = method.fields
    .filter((field) => field.location === 'query')
    .map((field) => [field.pythonName, field.wireName]);
  const bodyFields = method.fields
    .filter((field) => field.location === 'body')
    .map((field) => [field.pythonName, field.wireName]);
  generated.push(
    `${endpointName} = Endpoint(`,
    `    key=${JSON.stringify(`${method.namespace}.${method.tsName}`)},`,
    `    method=${JSON.stringify(method.verb)},`,
    `    path=${JSON.stringify(method.path)},`,
    `    path_fields=${pyTuple(pathFields)},`,
    `    query_fields=${pyTuple(queryFields)},`,
    `    body_fields=${pyTuple(bodyFields)},`,
    ')',
    '',
  );
}

for (const resource of resources) {
  generated.push(
    `class ${resource.className}(Resource):`,
    `    """${resource.namespace} endpoints."""`,
    '',
    resource.methods.map(methodSource).join('\n\n'),
    '',
    '',
  );
}

generated.push(
  'class ClientResources:',
  '    """Static namespace annotations for :class:`SpotifyApiClient`."""',
  '',
  ...resources.map(
    (resource) => `    ${resource.namespace}: ${resource.className}`,
  ),
  '',
  '',
  'RESOURCE_CLASSES: Dict[str, Type[Resource]] = {',
  ...resources.map(
    (resource) => `    ${JSON.stringify(resource.namespace)}: ${resource.className},`,
  ),
  '}',
  '',
);

fs.writeFileSync(outputPath, `${generated.join('\n')}\n`, 'utf8');

const reference = [
  '# API reference',
  '',
  'Generated from the canonical TypeScript SDK and OpenAPI contract.',
  'Pythonic `snake_case` methods also expose their npm-compatible `camelCase` aliases.',
  '',
];
for (const resource of resources) {
  reference.push(`## \`${resource.namespace}\``, '');
  for (const method of resource.methods) {
    const required = method.fields
      .filter((field) => field.required)
      .map((field) => field.pythonName);
    const optional = method.fields
      .filter((field) => !field.required)
      .map((field) => `${field.pythonName}=None`);
    if (method.genericBody) optional.unshift('body=None');
    if (method.genericQuery) optional.unshift('query=None');
    const args = [...required, ...optional].join(', ');
    const alias = method.tsName !== method.pythonName
      ? ` (alias: \`${method.tsName}\`)`
      : '';
    reference.push(
      `- \`${method.pythonName}(${args})\`${alias} — `
      + `${method.verb} \`${method.path}\``,
    );
  }
  reference.push('');
}
fs.writeFileSync(referencePath, `${reference.join('\n')}\n`, 'utf8');

console.log(
  `Generated ${methods.length} methods across ${resources.length} namespaces.`,
);
