from typing import Protocol


class LLMAdapter(Protocol):

    def complete(self, prompt: str) -> str:
        ...
