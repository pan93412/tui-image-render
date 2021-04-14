from PIL import Image
import asyncio
from tui.processors import generate_frame, GenerateFrameConfiguration
from tui.renders.Terminal import Terminal

async def main():
    terminal = Terminal()

    for i in range(1, 5302):
        img = Image.open(f"../frames2/frame{i}.jpg")
        frame = generate_frame(img, GenerateFrameConfiguration())
        terminal.render_frame(frame)


asyncio.run(main())
