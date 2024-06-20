from .queue_handler import ImageQueue

class Carousel:

    def __init__(self) -> None:
        pass

    @staticmethod
    def consume() -> str:
        return ImageQueue.get_from_queue()