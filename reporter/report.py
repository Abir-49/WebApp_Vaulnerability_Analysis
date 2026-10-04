

from collections.abc import Iterable

from verifier.models import VerifiedFinding


def render_markdown(findings: Iterable[VerifiedFinding]) -> str:
    finding_list = list(findings)
    return "# Assessment Report\n\nFindings: {}\n".format(len(finding_list))
