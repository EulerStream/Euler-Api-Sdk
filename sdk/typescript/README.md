# EulerStream TypeScript SDK

This is an API wrapper for the Euler Stream API written in TypeScript. 
With this API you can access any Euler Stream public endpoint. 

## Getting Started

Getting started is super simple! Remember to check out the OpenAPI Spec on the Euler Stream website at https://www.eulerstream.com/docs/openapi. 

For your convenience, we have included a hello-world example using this SDK:

1. Install the package with `npm i @eulerstream/euler-api-sdk`
2. Run the script below:


```ts
import EulerStreamApiClient, {IListAlertsResponse, IPipResponse} from "@eulerstream/euler-api-sdk";
import {AxiosResponse} from "axios";

// Initialize the client
const client = new EulerStreamApiClient(
    {apiKey: 'YOUR_API_KEY'}
);

// Fetch an endpoint
client.webcast.fetchWebcastURL('ttlive-node', undefined, 'tv_asahi_news').then((res: AxiosResponse<any>) => console.log("Got Webcast Fetch:", res.status, "Length:", JSON.stringify(res?.data).length));
```
