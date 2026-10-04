from dataclasses import dataclass
from enum import StrEnum


class VerificationStatus(StrEnum):

    CONFIRMED = "confirmed"
    INCONCLUSIVE = "inconclusive"
    NOT_PRESENT = "not_present"


@dataclass(frozen=True)
class VerifiedFinding:

    title: str
    status: VerificationStatus
    explanation: str


def verify_finding(finding: dict[str, str]) -> VerifiedFinding:
    _ = finding
    return VerifiedFinding(
        title="Unverified finding",
        status=VerificationStatus.INCONCLUSIVE,
        explanation="Verification logic has not been implemented yet.",
    )
