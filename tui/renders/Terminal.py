from typing import NamedTuple
from .Renders import Renders, Frames, Frame
import time

class TerminalConfiguration(NamedTuple):
    fps: int = 60

class Terminal(Renders):
    fps: int = 60

    def configure(self, configration: TerminalConfiguration):
        self.fps = configration.fps

    def render(self, frames: Frames) -> None:
        for frame in frames:
            self.render_frame(frame)

    def render_frame(self, frame: Frame) -> None:
        fps = self.fps

        # print the frame
        print(frame)
        # 1 FPS = 1/1000 second (maybe?)
        time.sleep(fps / 1000)
        # clear screen
        print("\x1b[2J")