import * as fs from 'fs';
import * as path from 'path';
import { ParsedOperation, ParamInfo, SpecOperation, SdkTransformer } from './transformers/types';
import { transformer as tsTransformer } from './transformers/typescript-sdk';
import { transformer as javaTransformer } from './transformers/java-sdk';
import { transformer as goTransformer } from './transformers/go-sdk';
import { transformer as csharpTransformer } from './transformers/csharp-sdk';
import { transformer as pythonTransformer, extractPythonOperations } from './transformers/python-sdk';

const ROOT = path.resolve(__dirname, '..');
const DOCS_DIR = path.resolve(__dirname, 'docs');
const OUTPUT_DIR = path.resolve(__dirname, 'output');
const SPEC_PATH = path.resolve(ROOT, 'build', 'openapi.json');

// ─── SDK Configurations ─────────────────────────────────────────────────────

interface SdkConfig {
  slug: string;
  /** Glob suffix to identify API doc files (e.g. "*Api.md") */
  apiFilePattern: RegExp;
  transformer: SdkTransformer;
  overridesPath: string | null;
  /** For SDKs whose docs live in a subfolder within the copied docs dir */
  docsSubdir?: string;
  /** Special extraction mode */
  mode: 'markdown' | 'python-source';
}

const SDKS: SdkConfig[] = [
  {
    slug: 'typescript',
    apiFilePattern: /Api\.md$/,
    transformer: tsTransformer,
    overridesPath: path.join(ROOT, 'sdk', 'typescript', 'overrides.json'),
    mode: 'markdown',
  },
  {
    slug: 'java',
    apiFilePattern: /Api\.md$/,
    transformer: javaTransformer,
    overridesPath: path.join(ROOT, 'sdk', 'java', 'overrides.json'),
    mode: 'markdown',
  },
  {
    slug: 'go',
    apiFilePattern: /API\.md$/,
    transformer: goTransformer,
    overridesPath: path.join(ROOT, 'sdk', 'go', 'overrides.json'),
    mode: 'markdown',
  },
  {
    slug: 'csharp',
    apiFilePattern: /Api\.md$/,
    transformer: csharpTransformer,
    overridesPath: path.join(ROOT, 'sdk', 'csharp', 'overrides.json'),
    mode: 'markdown',
  },
  {
    slug: 'python',
    apiFilePattern: /\.py$/,
    transformer: pythonTransformer,
    overridesPath: null,
    mode: 'python-source',
  },
];

// ─── OpenAPI Spec Loader ────────────────────────────────────────────────────

function loadSpec(): Map<string, SpecOperation> {
  const specContent = fs.readFileSync(SPEC_PATH, 'utf-8');
  const spec = JSON.parse(specContent);
  const ops = new Map<string, SpecOperation>();

  for (const [urlPath, methods] of Object.entries(spec.paths as Record<string, any>)) {
    for (const [method, opDef] of Object.entries(methods as Record<string, any>)) {
      if (!opDef.operationId) continue;
      ops.set(opDef.operationId.toLowerCase(), {
        operationId: opDef.operationId,
        tag: opDef.tags?.[0] || 'Unknown',
        method: method.toUpperCase(),
        path: urlPath,
        parameters: opDef.parameters || [],
        hasBody: !!opDef.requestBody,
        description: opDef.description,
      });
    }
  }

  return ops;
}

// ─── Markdown Parser ────────────────────────────────────────────────────────

function parseApiMarkdown(content: string, apiClassName: string): ParsedOperation[] {
  const operations: ParsedOperation[] = [];

  // Split content into operation sections.
  // TypeScript/Java/C#: "# **methodName**"
  // Go: "## MethodName"
  const sectionSplitRegex = /(?=^#{1,2}\s+\**\w+\**\s*$)/gm;
  const sections = content.split(sectionSplitRegex).filter(s => s.trim());

  for (const section of sections) {
    // Extract method name from the header
    const headerMatch = section.match(/^#{1,2}\s+\*{0,2}(\w+)\*{0,2}\s*$/m);
    if (!headerMatch) continue;

    const methodName = headerMatch[1];

    // Skip non-operation headers
    if (/^(Parameters|Example|Authorization|Return|HTTP|Path|Other)$/i.test(methodName)) continue;
    // Skip the file title header (same as apiClassName or contains namespace)
    if (methodName === apiClassName) continue;
    if (section.trimStart().startsWith('# ' + apiClassName)) continue;

    // Extract signature ("> ReturnType MethodName(...)")
    const sigMatch = section.match(/^>\s*(.+)$/m);
    const signature = sigMatch ? sigMatch[1].trim() : '';

    // Extract code block
    const codeMatch = section.match(/```\w+\n([\s\S]*?)```/);
    const rawExample = codeMatch ? codeMatch[1].trim() : '';

    // Extract parameters from markdown table
    const parameters = parseParamsTable(section);

    operations.push({
      methodName,
      apiClassName,
      signature,
      rawExample,
      parameters,
    });
  }

  return operations;
}

function parseParamsTable(section: string): ParamInfo[] {
  const params: ParamInfo[] = [];

  // Find the Parameters table (markdown table after "### Parameters" or "### Other Parameters")
  const tableMatch = section.match(
    /###\s+(?:Other\s+)?Parameters[\s\S]*?\n(\|.+\|[\s\S]*?)(?=\n###|\n\[|$)/
  );
  if (!tableMatch) return params;

  const tableContent = tableMatch[1];
  const rows = tableContent.split('\n').filter(r => r.includes('|'));

  // Skip header row and separator row
  for (let i = 2; i < rows.length; i++) {
    const cells = rows[i].split('|').map(c => c.trim()).filter(Boolean);
    if (cells.length < 2) continue;

    const name = cells[0].replace(/\*\*/g, '').trim();
    const type = cells[1].replace(/\*\*/g, '').replace(/\[.*?\]\(.*?\)/g, '').trim();
    const description = cells[2]?.replace(/\\'/g, "'") || '';
    const notes = cells[3] || '';

    params.push({
      name,
      type,
      description,
      optional: notes.includes('optional') || description.includes('(optional)'),
      defaultValue: extractDefault(notes + ' ' + description),
    });
  }

  return params;
}

function extractDefault(text: string): string | undefined {
  const match = text.match(/default(?:s?\s+to|:\s*)\s*['"]?([^'")\]\s,]+)/i);
  return match ? match[1] : undefined;
}

// ─── File Discovery ─────────────────────────────────────────────────────────

function findApiDocFiles(docsDir: string, pattern: RegExp, subdir?: string): string[] {
  const searchDir = subdir ? path.join(docsDir, subdir) : docsDir;
  if (!fs.existsSync(searchDir)) return [];

  return fs.readdirSync(searchDir)
    .filter(f => pattern.test(f))
    .map(f => path.join(searchDir, f));
}

function extractApiClassName(filePath: string, slug: string): string {
  const basename = path.basename(filePath, '.md');

  // For C#, docs might have namespace prefix in the first line
  // but the filename is just the class name
  if (slug === 'csharp-sdk') return basename;

  // For Go, strip leading backslash from content (file title has \AnalyticsAPI)
  return basename;
}

// ─── Main ───────────────────────────────────────────────────────────────────

function main() {
  console.log('Loading OpenAPI spec...');
  const specOps = loadSpec();
  console.log(`Found ${specOps.size} operations in spec.\n`);

  fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  for (const sdk of SDKS) {
    console.log(`\n── Processing ${sdk.slug} ──`);

    const docsDir = path.join(DOCS_DIR, sdk.slug);
    if (!fs.existsSync(docsDir)) {
      console.log(`  Docs dir not found: ${docsDir} — skipping.`);
      continue;
    }

    // Load overrides
    const overrides: Record<string, string> = sdk.overridesPath && fs.existsSync(sdk.overridesPath)
      ? JSON.parse(fs.readFileSync(sdk.overridesPath, 'utf-8'))
      : {};

    const result: Record<string, string> = {};

    if (sdk.mode === 'python-source') {
      // Special handling for Python: scan .py source modules
      const ops = extractPythonOperations(docsDir);
      console.log(`  Found ${ops.length} Python operations.`);

      for (const op of ops) {
        // Map to canonical operationId
        const canonicalId = resolveOperationId(op.methodName, specOps, 'python');
        if (!canonicalId) {
          console.log(`  WARN: No spec match for Python module "${op.methodName}"`);
          continue;
        }

        const example = sdk.transformer.transform(op, overrides);
        result[canonicalId] = example;
      }
    } else {
      // Markdown-based SDKs
      const docFiles = findApiDocFiles(docsDir, sdk.apiFilePattern, sdk.docsSubdir);
      console.log(`  Found ${docFiles.length} API doc files.`);

      for (const docFile of docFiles) {
        const content = fs.readFileSync(docFile, 'utf-8');
        const apiClassName = extractApiClassName(docFile, sdk.slug);
        const operations = parseApiMarkdown(content, apiClassName);

        console.log(`  ${path.basename(docFile)}: ${operations.length} operations`);

        for (const op of operations) {
          // Map method name to canonical operationId from spec
          const canonicalId = resolveOperationId(op.methodName, specOps, sdk.slug);
          if (!canonicalId) {
            console.log(`    WARN: No spec match for "${op.methodName}"`);
            continue;
          }

          const example = sdk.transformer.transform(op, overrides);
          result[canonicalId] = example;
        }
      }
    }

    // Write output
    const outputPath = path.join(OUTPUT_DIR, `${sdk.slug}.json`);
    fs.writeFileSync(outputPath, JSON.stringify(result, null, 2) + '\n', 'utf-8');
    console.log(`  Wrote ${Object.keys(result).length} examples to ${path.basename(outputPath)}`);
  }

  console.log('\nDone.');
}

/**
 * Map a SDK-specific method name to the canonical operationId from the OpenAPI spec.
 * Handles casing differences: camelCase (TS/Java), PascalCase (Go/C#), snake_case (Python).
 */
function resolveOperationId(
  methodName: string,
  specOps: Map<string, SpecOperation>,
  sdkSlug: string,
): string | null {
  // Direct case-insensitive match
  const lower = methodName.toLowerCase();
  if (specOps.has(lower)) return specOps.get(lower)!.operationId;

  // For Python, convert snake_case to lowercase run-together
  if (sdkSlug === 'python-sdk') {
    const collapsed = methodName.replace(/_/g, '').toLowerCase();
    if (specOps.has(collapsed)) return specOps.get(collapsed)!.operationId;

    // Also try PascalCase → lowercase
    for (const [key, op] of specOps) {
      if (key === collapsed) return op.operationId;
    }
  }

  // Fallback: try matching by stripping non-alpha and comparing
  const stripped = methodName.replace(/[^a-zA-Z]/g, '').toLowerCase();
  for (const [key, op] of specOps) {
    if (key.replace(/[^a-z]/g, '') === stripped) return op.operationId;
  }

  return null;
}

main();
