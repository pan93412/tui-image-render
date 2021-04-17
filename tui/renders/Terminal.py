from typing import NamedTuple
from .Renders import Renders, Frames, Frame
from ..logger import logger
import time

class TerminalConfiguration(NamedTuple):
    fps: int = 60

class Terminal(Renders):
    fps: int = 60

    def configure(self, configration: TerminalConfiguration):
        logger.debug(" -> Terminal.configure()")
        self.fps = configration.fps
        logger.debug(" <- Terminal.configure()")


    def render(self, frames: Frames) -> None:
        logger.debug(" -> Terminal.render()")

        map(self.render_frame, frames)

        logger.info("All frames are rendered.")
        logger.debug(" <- Terminal.render()")

    def render_frame(self, frame: Frame) -> None:
        logger.debug(" -> Terminal.render_frame()")

        logger.debug("reading fps from Terminal object")
        fps = self.fps

        # print the frame
        logger.debug("printing frame")
        print(frame)
        logger.debug("sleep and wait the next frame")
        # 1 FPS = 1/1000 second (maybe?)
        time.sleep(fps / 1000)
        logger.debug("clearing screen")
        # clear screen
        print("\x1b[2J")

        logger.info("Rendered 1 frame.")
        logger.debug(" <- Terminal.render_frame()")
