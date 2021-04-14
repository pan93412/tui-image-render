from abc import ABC, abstractmethod
from typing import Any

Frames = list[str]

class Renders(ABC):
    def configure(self, configration: Any):
        pass

    @abstractmethod
    def render(self, frames: Frames):
        pass
