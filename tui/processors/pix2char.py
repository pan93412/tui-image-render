from PIL.Image import Image

'''
Consts: The sample of the image.
'''
SAMPLE = 24

def pix2char(image: Image, table: list[str]) -> str:
    pixels = image.getdata()
    mapped_pixels = map(lambda pixel: table[pixel // SAMPLE], pixels)
    characters = "".join(mapped_pixels)
    return characters
