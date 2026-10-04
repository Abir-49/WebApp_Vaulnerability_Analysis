# Adaptive Web Application Vulnerability Assessment

Initial Python skeleton for the thesis project **Adaptive Web Application Vulnerability Assessment in an Isolated Sandbox, with Explainable Reporting**.

This repository currently contains the project structure, a runnable CLI, placeholder module APIs, and a basic Docker Compose target. It does not perform real crawling, exploitation, static analysis, LLM calls, verification, or report generation yet.

## Requirements

- Python 3.11 or newer
- Docker Desktop with Docker Compose
- Windows PowerShell or Command Prompt

## Setup

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Run the CLI

```powershell
python main.py http://localhost:3000
python main.py http://localhost:3000 --mode url+codebase
```

The CLI validates the URL, accepts the planned assessment mode, and logs the received configuration. Scanning is intentionally not implemented yet.

## Start the local target

```powershell
docker compose up -d
docker compose ps
```

Open http://localhost:3000 after Juice Shop reports `Server listening on port 3000`. Stop it with:

```powershell
docker compose down
```

This is only a basic local container setup, not the final thesis isolation or network-segmentation design. Test only applications you own or are authorized to assess.

## Structure

- `config/`: settings and configuration
- `sandbox/`: future Docker lifecycle and isolation controls
- `discovery/`: future crawler and endpoint discovery
- `static_analysis/`: future Semgrep integration
- `llm_adapter/`: future OpenAI-compatible/Ollama adapter boundary
- `prioritizer/`: future features, scoring, and history
- `executor/`: future SQLi, XSS, IDOR, and path-traversal tests
- `verifier/`: future finding verification
- `reporter/`: future explainable reports
- `main.py`: CLI entry point
- `tests/`: initial CLI tests

See [BEGINNER_GUIDE.md](BEGINNER_GUIDE.md) for explanations of Python, virtual environments, Docker, `__pycache__`, `pyproject.toml`, and the project workflow.

## Checks

```powershell
python -m compileall .
python -m pytest -q
```
