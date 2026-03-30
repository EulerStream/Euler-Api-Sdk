import * as fs from 'fs';
import * as path from 'path';
import { ParsedOperation, SdkTransformer } from './types';

/**
 * Generate Python examples from the openapi-python-client module structure.
 * Python SDK has NO markdown docs — examples are synthesized from module files.
 *
 * Target pattern:
 *   from EulerApiSdk import AuthenticatedClient
 *   from EulerApiSdk.api.tik_tok_live import retrieve_room_id
 *
 *   client = AuthenticatedClient(
 *       base_url="https://tiktok.eulerstream.com",
 *       token="YOUR_API_KEY",
 *   )
 *
 *   result = retrieve_room_id.sync(client=client, unique_id="@username")
 */

/** Convert PascalCase/camelCase operationId to snake_case module name */
export function toSnakeCase(str: string): string {
  return str
    .replace(/([A-Z])/g, '_$1')
    .toLowerCase()
    .replace(/^_/, '');
}

/** Map an API tag to the Python module directory name */
const TAG_TO_MODULE: Record<string, string> = {
  'TikTok LIVE': 'tik_tok_live',
  'Accounts': 'accounts',
  'Authentication': 'authentication',
  'Analytics': 'analytics',
  'Alerts': 'tik_tok_live_alerts',
  'Alert Targets': 'tik_tok_live_alert_targets',
  'Captchas': 'tik_tok_captchas',
};

/**
 * Scan the Python SDK source to extract operations.
 * Returns ParsedOperation[] built from the .py module files.
 */
export function extractPythonOperations(pythonDocsDir: string): ParsedOperation[] {
  const operations: ParsedOperation[] = [];

  if (!fs.existsSync(pythonDocsDir)) return operations;

  for (const tagDir of fs.readdirSync(pythonDocsDir)) {
    const tagPath = path.join(pythonDocsDir, tagDir);
    if (!fs.statSync(tagPath).isDirectory()) continue;
    if (tagDir === '__pycache__' || tagDir.startsWith('.')) continue;

    for (const file of fs.readdirSync(tagPath)) {
      if (!file.endsWith('.py') || file.startsWith('__')) continue;

      const moduleName = file.replace('.py', '');
      const filePath = path.join(tagPath, file);
      const content = fs.readFileSync(filePath, 'utf-8');

      // Extract params from the sync() function signature
      const syncMatch = content.match(/def sync\(\s*\*,\s*client:\s*\w+,?\s*([\s\S]*?)\)\s*->/);
      const params: ParsedOperation['parameters'] = [];

      if (syncMatch && syncMatch[1].trim()) {
        const paramBlock = syncMatch[1];
        for (const line of paramBlock.split('\n')) {
          const pMatch = line.trim().match(/^(\w+):\s*(.+?)(?:\s*=\s*(.+))?,?\s*$/);
          if (pMatch) {
            params.push({
              name: pMatch[1],
              type: pMatch[2].trim().replace(/,$/, ''),
              description: '',
              optional: !!pMatch[3],
              defaultValue: pMatch[3]?.trim(),
            });
          }
        }
      }

      // Convert module name back to operationId (best-effort PascalCase)
      const operationId = moduleName
        .split('_')
        .map(w => w.charAt(0).toUpperCase() + w.slice(1))
        .join('');

      operations.push({
        methodName: moduleName,
        apiClassName: tagDir,
        signature: '',
        rawExample: '',
        parameters: params,
      });
    }
  }

  return operations;
}

function buildKwargs(params: ParsedOperation['parameters']): string {
  if (params.length === 0) return '';
  return params.map(p => {
    switch (p.type) {
      case 'str': return `${p.name}="${p.name}_value"`;
      case 'float':
      case 'int': return `${p.name}=0`;
      case 'bool': return `${p.name}=True`;
      default: return `${p.name}=${p.name}_value`;
    }
  }).join(', ');
}

export const transformer: SdkTransformer = {
  transform(op: ParsedOperation, _overrides: Record<string, string>): string {
    const moduleDir = op.apiClassName; // Already the snake_case dir name
    const moduleName = op.methodName; // Already the snake_case module name
    const kwargs = buildKwargs(op.parameters);
    const callArgs = kwargs ? `client=client, ${kwargs}` : 'client=client';

    const lines = [
      `from EulerApiSdk import AuthenticatedClient`,
      `from EulerApiSdk.api.${moduleDir} import ${moduleName}`,
      ``,
      `client = AuthenticatedClient(`,
      `    base_url="https://tiktok.eulerstream.com",`,
      `    token="YOUR_API_KEY",`,
      `)`,
      ``,
      `result = ${moduleName}.sync(${callArgs})`,
    ];

    return lines.join('\n');
  },
};
