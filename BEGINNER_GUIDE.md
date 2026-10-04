# Beginner Guide

This project is a Python skeleton for a thesis about testing intentionally vulnerable web applications inside a controlled Docker environment. The real scanner is not implemented yet.

## Python

Python is the programming language used by this project. A `.py` file contains Python instructions. The Python interpreter runs those instructions:

```powershell
python main.py http://localhost:3000
```

`main.py` is the program file and `http://localhost:3000` is an argument passed to it.

## Virtual environments

A virtual environment is a private package area for one project. It prevents packages for different projects from conflicting.

Create one on Windows:

```powershell
py -3.11 -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install this project's packages:

```powershell
python -m pip install -r requirements.txt
```

Leave the environment with:

```powershell
deactivate
```

The `.venv` folder is generated local tooling, not source code, so `.gitignore` excludes it.

## pip and requirements.txt

`pip` installs Python packages. A package is reusable code written by somebody else.

[requirements.txt](requirements.txt) lists this project's packages:

- `requests`: HTTP requests
- `beautifulsoup4`: HTML parsing
- `pydantic`: structured data validation
- `python-dotenv`: environment configuration
- `semgrep`: planned code analysis
- `pytest`: automated tests

Install the list with:

```powershell
python -m pip install -r requirements.txt
```

## `__pycache__`

Python may create `__pycache__` folders containing `.pyc` helper files. They are generated automatically, are not your source code, and can be deleted and recreated. `.gitignore` keeps them out of Git.

## Modules and packages

A module is usually one Python file. A package is a folder containing related modules and an `__init__.py` file.

This project uses these packages:

- `config`: configuration
- `sandbox`: future Docker lifecycle and isolation
- `discovery`: future crawler and endpoint discovery
- `static_analysis`: future Semgrep integration
- `llm_adapter`: future OpenAI-compatible or Ollama interface
- `prioritizer`: future adaptive feature extraction and scoring
- `executor`: future SQL injection, XSS, IDOR, and path traversal tests
- `verifier`: future finding confirmation
- `reporter`: future explainable reports

## Stubs

A stub is placeholder code. For example, `discovery/crawler.py` has a `crawl()` function that currently returns an empty list. This creates the correct place for future logic without claiming the logic is finished.

The executor files also have placeholder `run()` functions. They do not send attack payloads.

## `main.py`

[main.py](main.py) is the command-line entry point. It validates an HTTP or HTTPS target URL and accepts two modes:

```powershell
python main.py http://localhost:3000
python main.py http://localhost:3000 --mode url+codebase
```

`url-only` is the planned black-box mode. It uses only web-visible behavior. `url+codebase` is the planned grey-box mode. It may also inspect source code with Semgrep.

The current CLI only prints the received settings.

## Docker

Docker runs applications inside containers. A container is an isolated process environment containing an application and its dependencies. This project uses Docker because the practice targets are intentionally vulnerable.

Docker is not automatically perfect security. The final thesis should add network restrictions, resource limits, cleanup, logging, and other controls.

## Docker Compose

[docker-compose.yml](docker-compose.yml) describes an OWASP Juice Shop container:

```yaml
services:
  target:
    image: bkimminich/juice-shop:latest
    container_name: apt-juice-shop
    ports:
      - "3000:3000"
```

Start it:

```powershell
docker compose up -d
```

Check it:

```powershell
docker compose ps
docker compose logs --tail=50 target
```

Open `http://localhost:3000`. The first startup may take 30 to 60 seconds. Wait for `Server listening on port 3000`, then refresh.

Stop it:

```powershell
docker compose down
```

## YAML

YAML is a configuration format. Docker Compose uses it. Indentation matters, so preserve the spaces in `docker-compose.yml`.

## `pyproject.toml`

[pyproject.toml](pyproject.toml) is standard Python tool configuration. In this project it tells pytest where tests are located and how imports should work:

```toml
[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

It is not the same thing as `requirements.txt`. `requirements.txt` lists installable packages; `pyproject.toml` configures tools and can later contain packaging metadata.

## Tests

[tests/test_main.py](tests/test_main.py) checks valid modes and invalid URLs. Run it with:

```powershell
python -m pytest -q
```

If `pytest` is missing, activate `.venv` and run `python -m pip install -r requirements.txt`.

## `.gitignore`

`.gitignore` tells Git not to upload generated or private files such as `.venv`, `__pycache__`, `.env`, logs, and reports. Never commit passwords or API keys.

## Project flow

The planned flow is:

```text
Target URL -> Sandbox -> Discovery -> Prioritizer -> Executor
                                                   |
                                                   v
                                               Verifier
                                                   |
                                                   v
                                               Reporter
```

In grey-box mode, static analysis will also provide source-code information. The LLM adapter will remain behind one interface so the project can later use an OpenAI-compatible service or Ollama without rewriting the rest of the code.

## Basic workflow

```powershell
cd C:\Users\User\Desktop\APT
.\.venv\Scripts\Activate.ps1
docker compose up -d
python main.py http://localhost:3000
python -m pytest -q
docker compose down
deactivate
```

Only test applications you own or have explicit permission to assess. OWASP Juice Shop is designed for legal security practice.
