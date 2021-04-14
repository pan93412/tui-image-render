from abc import ABC, abstractmethod
from typing import Any

'''
A frame.
'''
Frame = str
'''
A list of frames.
'''
Frames = list[Frame]

class Renders(ABC):
    def configure(self, configration: Any):
        pass

    @abstractmethod
    def render(self, frames: Frames):
        pass

    @abstractmethod
    def render_frame(self, frame: Frame):
        pass
