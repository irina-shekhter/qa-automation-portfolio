# QA Automation Portfolio

Test automation framework for the Restful Booker Platform - a microservice-based
B&B booking system used as a system under test.

**Status:** in progress - under active development.

## Stack

- Python 3.13, pytest
- httpx, pydantic - API client and response schema validation
- Playwright - browser automation
- Docker Compose - containerized system under test
- GitHub Actions - CI

## Running

```bash
uv sync
docker compose up -d
uv run pytest
```
