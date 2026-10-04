
from dataclasses import dataclass


@dataclass(frozen=True)
class AssessmentSettings:

    target_url: str
    mode: str = "url-only"
