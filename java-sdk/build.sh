#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p "$SCRIPT_DIR/build"

# Get the spec
wget -O "$SCRIPT_DIR/build/openapi.json" https://tiktok.eulerstream.com/dashboard/openapi

# Generate Java SDK
echo "Generating Java SDK..."
cd "$ROOT_DIR"
npx @openapitools/openapi-generator-cli generate \
  -i ./java-sdk/build/openapi.json \
  -g java \
  -o ./java-sdk/src/generated \
  --additional-properties=groupId=com.eulerstream,artifactId=euler-api-sdk,apiPackage=com.eulerstream.api,modelPackage=com.eulerstream.model,invokerPackage=com.eulerstream

# Render the client wrapper from template
echo "Rendering EulerStreamApiClient.java from template..."
cd "$SCRIPT_DIR"
npx tsx ./render-template.ts
