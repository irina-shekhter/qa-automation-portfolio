# QA Automation Portfolio

API and E2E test automation framework built with Python.

**Status:** in progress — under active development.

## Stack

- Python 3.13, pytest
- httpx, pydantic — API client and schema validation
- Playwright — browser automation
- Docker Compose — containerized system under test
- GitHub Actions — CI

## Running

```bash
uv sync
docker compose up -d
uv run pytest
```