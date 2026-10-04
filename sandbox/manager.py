

class SandboxManager:

    def start_target(self, image: str) -> None:
        raise NotImplementedError("Sandbox lifecycle is planned but not implemented")

    def stop_target(self) -> None:
        raise NotImplementedError("Sandbox lifecycle is planned but not implemented")
