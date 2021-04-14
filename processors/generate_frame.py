from tuiviewer.prog.utilities.sequence_table import create_sequenced_table
from typing import NamedTuple
from PIL.Image import Image
from .pix2char import pix2char
from .resize_gray_image import resize_gray_image, ResizeGrayImageConfigurations


class GenerateFrameConfiguration(NamedTuple):
    width: int = 70
    table: list[str] = create_sequenced_table()


def generate_frame(image: Image, configuration: GenerateFrameConfiguration) -> str:
    width, table = configuration.width, configuration.table

    new_image_data = pix2char(resize_gray_image(image, ResizeGrayImageConfigurations(width=width)), table)

    total_pixels = len(new_image_data)

    ascii_image = "\n".join([new_image_data[index:(index+width)]
                            for index in range(0, total_pixels, width)])

    return ascii_image
