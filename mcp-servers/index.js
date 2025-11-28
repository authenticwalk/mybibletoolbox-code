#!/usr/bin/env node

import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import {
    ListResourcesRequestSchema,
    ReadResourceRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import fs from "fs/promises";
import path from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const pdf = require("pdf-parse");
import mammoth from "mammoth";

const server = new Server(
    {
        name: "document-server",
        version: "1.0.0",
    },
    {
        capabilities: {
            tools: {},
        },
    }
);

server.setRequestHandler(ListResourcesRequestSchema, async () => {
    return {
        resources: [
            {
                uri: "pdf://internal/example",
                name: "Example PDF Resource",
                mimeType: "text/plain",
            },
        ],
    };
});

server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
    const uri = request.params.uri;

    if (uri.startsWith("pdf://")) {
        const filePath = uri.replace("pdf://", "");
        try {
            const dataBuffer = await fs.readFile(filePath);
            const data = await pdf(dataBuffer);
            return {
                contents: [
                    {
                        uri: uri,
                        mimeType: "text/plain",
                        text: data.text,
                    },
                ],
            };
        } catch (error) {
            throw new Error(`Error reading PDF ${filePath}: ${error.message}`);
        }
    }

    if (uri.startsWith("docx://")) {
        const filePath = uri.replace("docx://", "");
        try {
            const result = await mammoth.extractRawText({ path: filePath });
            return {
                contents: [
                    {
                        uri: uri,
                        mimeType: "text/plain",
                        text: result.value,
                    },
                ],
            };
        } catch (error) {
            throw new Error(`Error reading DOCX ${filePath}: ${error.message}`);
        }
    }

    throw new Error(`Unknown resource: ${uri}`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
