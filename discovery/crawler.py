

from dataclasses import dataclass


@dataclass(frozen=True)
class DiscoveredEndpoint:
    url: str
    method: str = "GET"


def crawl(start_url: str) -> list[DiscoveredEndpoint]:
    _ = start_url
    return []
