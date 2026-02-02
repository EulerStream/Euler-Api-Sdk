echo "Fetching latest OpenAPI spec from EulerStream..."

mkdir -p build

# Get the spec
wget -O ./build/openapi.json https://tiktok.eulerstream.com/dashboard/openapi

# Generate TypeScript
openapi-generator-cli generate -i ./build/openapi.json -g typescript-axios -o ./src/sdk

