import * as fs from 'fs';
import * as path from 'path';

/**
 * Fixes Go enum constant conflicts in OpenAPI-generated code.
 *
 * The Go generator creates unqualified constant names (e.g. `_0`, `DE`) that
 * collide when multiple enum types share the same values. This script prefixes
 * each constant with its type name to make them unique.
 *
 *   Before:  _0 AccountScopes = 0
 *   After:   ACCOUNT_SCOPES_0 AccountScopes = 0
 */

const GENERATED_DIR: string = process.argv[2] || path.resolve(__dirname, '..', 'generated');

// Convert PascalCase type name to SCREAMING_SNAKE_CASE prefix
function toPrefix(typeName: string): string {
    return typeName
        .replace(/([a-z])([A-Z])/g, '$1_$2')
        .replace(/([A-Z]+)([A-Z][a-z])/g, '$1_$2')
        .toUpperCase();
}

// Match a const block: `const (\n  NAME Type = value\n  ...\n)`
const constBlockRegex = /const \(\n([\s\S]*?)\n\)/g;
// Match a single constant line: `\tNAME Type = value`
const constLineRegex = /^\t(\w+)\s+(\w+)\s*=\s*(.+)$/;

let totalFixed = 0;

const files: string[] = fs.readdirSync(GENERATED_DIR)
    .filter((f: string) => f.startsWith('model_') && f.endsWith('.go'));

for (const file of files) {
    const filePath: string = path.join(GENERATED_DIR, file);
    const original: string = fs.readFileSync(filePath, 'utf-8');
    let modified: string = original;

    modified = modified.replace(constBlockRegex, (block: string) => {
        const lines: string[] = block.split('\n');
        const newLines: string[] = [lines[0]]; // "const ("

        for (let i = 1; i < lines.length; i++) {
            const line: string = lines[i];
            const match: RegExpMatchArray | null = line.match(constLineRegex);

            if (match) {
                const [, constName, typeName, value] = match;
                const prefix: string = toPrefix(typeName);
                const newName: string = `${prefix}_${constName.replace(/^_/, '')}`;
                newLines.push(`\t${newName} ${typeName} = ${value}`);
                totalFixed++;
            } else {
                newLines.push(line);
            }
        }

        return newLines.join('\n');
    });

    if (modified !== original) {
        fs.writeFileSync(filePath, modified, 'utf-8');
    }
}

// Also remove generated test directory (depends on testify which isn't in go.mod)
const testDir: string = path.join(GENERATED_DIR, 'test');
if (fs.existsSync(testDir)) {
    fs.rmSync(testDir, { recursive: true });
    console.log(`Removed generated test directory (requires testify)`);
}

console.log(`Fixed ${totalFixed} enum constants across ${files.length} model files`);
