import * as fs from 'fs';
import * as path from 'path';

/**
 * Fixes C# enum member name conflicts in OpenAPI-generated code.
 *
 * The C# generator creates enum member names like `_12` for both value -1
 * (ordinal 2) and value 12, causing duplicates. This script detects duplicate
 * enum members and appends `_v{ordinal}` to disambiguate.
 */

const MODEL_DIR: string = process.argv[2] ||
    path.resolve(__dirname, 'src/generated/src/EulerApiSdk/Model');

// Match a C# enum block
const enumBlockRegex = /public enum (\w+)\s*\{([\s\S]*?)\}/g;
// Match an enum member: `_Name = ordinal,`
const enumMemberRegex = /^(\s+)(\w+)(\s*=\s*\d+,?)$/;

let totalFixed = 0;

const files: string[] = fs.readdirSync(MODEL_DIR)
    .filter((f: string) => f.endsWith('.cs'));

for (const file of files) {
    const filePath: string = path.join(MODEL_DIR, file);
    const original: string = fs.readFileSync(filePath, 'utf-8');
    let modified: string = original;

    modified = modified.replace(enumBlockRegex, (fullMatch: string, enumName: string, body: string) => {
        const lines: string[] = body.split('\n');
        const seen = new Map<string, number>();
        const newLines: string[] = [];

        for (const line of lines) {
            const match: RegExpMatchArray | null = line.match(enumMemberRegex);
            if (match) {
                const [, indent, memberName, rest] = match;
                const count: number = seen.get(memberName) || 0;
                seen.set(memberName, count + 1);

                if (count > 0) {
                    // Duplicate — rename with suffix
                    const newName: string = `${memberName}_v${count + 1}`;
                    newLines.push(`${indent}${newName}${rest}`);
                    totalFixed++;

                    // Also fix the preceding summary comment if present
                    const prevIdx: number = newLines.length - 2;
                    if (prevIdx >= 0 && newLines[prevIdx].includes(`Enum ${memberName} for value`)) {
                        newLines[prevIdx] = newLines[prevIdx].replace(
                            `Enum ${memberName}`,
                            `Enum ${newName}`
                        );
                    }
                } else {
                    newLines.push(line);
                }
            } else {
                newLines.push(line);
            }
        }

        return `public enum ${enumName} {${newLines.join('\n')}}`;
    });

    if (modified !== original) {
        // Also fix references to renamed members in the rest of the file
        // The converter methods reference enum members like `EnumName.MemberName`
        fs.writeFileSync(filePath, modified, 'utf-8');
    }
}

console.log(`Fixed ${totalFixed} duplicate enum members across ${files.length} model files`);
