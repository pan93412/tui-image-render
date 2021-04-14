from PIL import Image
import asyncio
from processors import generate_frame, GenerateFrameConfiguration

async def main():
    frames: list[str] = []

    for i in range(1, 5302):
        img = Image.open(f"../frames2/frame{i}.jpg")
        frames.append(generate_frame(img, GenerateFrameConfiguration()))
        

asyncio.run(main())
