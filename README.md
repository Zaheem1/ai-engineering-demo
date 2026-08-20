# AI Engineering Demo

A minimal scaffold demonstrating an AI-powered service with:
- FastAPI backend (`app/main.py`)
- AI routing and release-notes generation logic (`app/ai/`)
- An MCP server (`app/mcp/server.py`)
- Tests (`tests/`)
- Cursor rules for consistent AI-assisted development (`.cursor/rules/`)
- CI workflow (`.github/workflows/test.yml`)
- Docker Compose setup for local development

## Getting Started

```bash
cp .env.example .env
docker compose up --build
```

## Project Structure

```
ai-engineering-demo/
├── app/
│   ├── main.py           # FastAPI entrypoint
│   ├── ai/
│   │   ├── router.py          # Routes requests to the right AI logic
│   │   └── release_notes.py   # Release notes generation logic
│   └── mcp/
│       └── server.py     # MCP server implementation
├── tests/
│   └── test_release_notes.py
├── .cursor/rules/         # Cursor AI coding rules
├── .github/workflows/     # CI pipelines
├── docker-compose.yml
└── .env.example
```
# ai-engineering-demo
