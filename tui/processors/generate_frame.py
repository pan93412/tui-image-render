from ..logger import logger
from ..utilities.sequence_table import create_sequenced_table
from typing import NamedTuple
from PIL.Image import Image
from .pix2char import pix2char
from .resize_gray_image import resize_gray_image, ResizeGrayImageConfigurations

class GenerateFrameConfiguration(NamedTuple):
    width: int = 70
    table: list[str] = create_sequenced_table()


def generate_frame(image: Image, configuration: GenerateFrameConfiguration) -> str:
    logger.debug(" -> generate_frame()")
    logger.debug("getting width and table from configuration")
    width, table = configuration.width, configuration.table

    logger.debug("getting new_image_data with resize_gray_image() and pix2char()")
    new_image_data = pix2char(resize_gray_image(image, ResizeGrayImageConfigurations(width=width)), table)

    logger.debug("calculating total_pixels")
    total_pixels = len(new_image_data)

    logger.debug("getting ascii_image")
    ascii_image = "\n".join([new_image_data[index:(index+width)]
                            for index in range(0, total_pixels, width)])

    logger.info("Generated a frame!")
    logger.debug(" <- generate_frame()")
    return ascii_image
