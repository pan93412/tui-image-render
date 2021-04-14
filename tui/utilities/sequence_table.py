from ..logger import logger

def create_sequenced_table(length: int = 128) -> list[str]:
    logger.debug("creating sequenced table")
    return [str(i) for i in range(0, length)]
