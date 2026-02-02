import 'dotenv/config';
import {execSync} from 'child_process';
import * as readline from "node:readline";

// Load .env (already done via dotenv/config import)

// Wait for user to press any key
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question('Press any key to upload...', () => {
  rl.close();

  try {
    // Set npm auth token
    const npmToken = process.env.NPM_TOKEN;
    if (!npmToken) {
      throw new Error('NPM_TOKEN not found in environment variables.');
    }

    execSync(
        `pnpm config set //registry.npmjs.org/:_authToken=${npmToken} && pnpm publish --no-git-checks --access public --registry https://registry.npmjs.org/`
        , { stdio: 'inherit' }
    );

    console.log('Package published successfully.');
  } catch (error) {
    console.error('Error:', error);
    process.exit(1);
  }
});
