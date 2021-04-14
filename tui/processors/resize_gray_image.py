from typing import NamedTuple
from PIL.Image import Image
from ..logger import logger

class ResizeGrayImageConfigurations(NamedTuple):
    width: int = 70
    height: int = 20

def resize_gray_image(image: Image, configuration: ResizeGrayImageConfigurations) -> Image:
    logger.debug(" -> resize_gray_image()")

    logger.debug("resizing image and convert to L");
    resized_gray_image = image.resize((configuration.width, configuration.height)).convert('L')

    logger.debug(" <- resize_gray_image()")
    return resized_gray_image
