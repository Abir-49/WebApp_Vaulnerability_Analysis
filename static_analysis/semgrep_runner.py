

from dataclasses import dataclass


@dataclass(frozen=True)
class StaticFinding:

    rule_id: str
    message: str
    file_path: str
    line: int | None = None


def run_semgrep(codebase_path: str) -> list[StaticFinding]:
    _ = codebase_path
    return []
