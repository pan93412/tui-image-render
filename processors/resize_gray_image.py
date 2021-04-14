from typing import NamedTuple
from PIL.Image import Image

class ResizeGrayImageConfigurations(NamedTuple):
    width: int = 70
    height: int = 20

def resize_gray_image(image: Image, configuration: ResizeGrayImageConfigurations) -> Image:
    resized_gray_image = image.resize((configuration.width, configuration.height)).convert('L')
    return resized_gray_image
