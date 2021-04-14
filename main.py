from PIL import Image
import asyncio
import time

ASCII_CHARS = [".", ",", ":", ";"] + [f"{str(i)}" for i in range(1, 256)]

def resized_gray_image(image: Image.Image, new_width: int = 70) -> Image.Image:
    new_height = 20
    resized_gray_image = image.resize((new_width, new_height)).convert('L')
    return resized_gray_image


def pix2chars(image: Image.Image) -> str:
    pixels = image.getdata()
    characters = "".join(map(lambda pixel: ASCII_CHARS[pixel // 24], pixels))
    return characters


def generate_frame(image: Image.Image, new_width: int = 70) -> str:
    new_image_data = pix2chars(resized_gray_image(image, new_width=new_width))

    total_pixels = len(new_image_data)

    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                            for index in range(0, total_pixels, new_width)])

    return ascii_image

def generate_all_frames():
async def main():
    for i in range(1, 5302):
        img = Image.open(f"frames2/frame{i}.jpg")  # type: ignore
        frame = generate_frame(img, 60)  # type: ignore
        if frame is not None:
            print(frame)
            # 60fps is about 16ms per picture
            time.sleep(0.016)
        print("\x1b[2J")

asyncio.run(main())
