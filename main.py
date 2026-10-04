from __future__ import annotations

import argparse
import logging
from urllib.parse import urlparse


LOGGER = logging.getLogger("apt")


def validate_target_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise argparse.ArgumentTypeError(
            "target must be an absolute URL starting with http:// or https://"
        )
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Adaptive web application vulnerability assessment skeleton"
    )
    parser.add_argument(
        "target_url",
        type=validate_target_url,
        help="Base URL of the intentionally vulnerable target application",
    )
    parser.add_argument(
        "--mode",
        choices=("url-only", "url+codebase"),
        default="url-only",
        help="Assessment mode (default: url-only)",
    )
    return parser


def main() -> int:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    args = build_parser().parse_args()
    LOGGER.info("Target URL: %s", args.target_url)
    LOGGER.info("Assessment mode: %s", args.mode)
    LOGGER.info("Scanning is not implemented yet; project skeleton is ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
