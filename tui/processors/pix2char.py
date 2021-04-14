from PIL.Image import Image
from ..logger import logger

'''
Consts: The sample of the image.
'''
SAMPLE = 24

def pix2char(image: Image, table: list[str]) -> str:
    logger.debug(" -> pix2char()")

    logger.debug("getting pixels from image.getdata()")
    pixels = image.getdata()
    logger.debug("mapping pixels")
    mapped_pixels = map(lambda pixel: table[pixel // SAMPLE], pixels)
    logger.debug("getting characters")
    characters = "".join(mapped_pixels)

    logger.debug(" <- pix2char()")
    return characters
