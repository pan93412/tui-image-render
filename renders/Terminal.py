from typing import NamedTuple
from .Renders import Renders, Frames
import time

class TerminalConfiguration(NamedTuple):
    fps: int = 60

class Terminal(Renders):
    fps: int = 60

    def configure(self, configration: TerminalConfiguration):
        self.fps = configration.fps

    def render(self, frames: Frames):
        fps = self.fps

        for frame in frames:
            # print the frame
            print(frame)
            # 1 FPS = 1/1000 second (maybe?)
            time.sleep(fps / 1000)
        
        # clear screen
        print("\x1b[2J")
