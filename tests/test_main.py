

import pytest

from main import build_parser


def test_parser_accepts_url_only_mode() -> None:
    args = build_parser().parse_args(["http://localhost:3000"])
    assert args.target_url == "http://localhost:3000"
    assert args.mode == "url-only"


def test_parser_accepts_codebase_mode() -> None:
    args = build_parser().parse_args(
        ["https://example.test", "--mode", "url+codebase"]
    )
    assert args.mode == "url+codebase"


def test_parser_rejects_non_http_url() -> None:
    with pytest.raises(SystemExit):
        build_parser().parse_args(["localhost:3000"])
