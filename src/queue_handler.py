from queue import Queue

class ImageQueue:

    image_queue = Queue(maxsize = 3)

    def __init__(self):
        pass
        # ImageQueue.image_queue = Queue(maxsize = 50)
        # Need to give a max size otherwise program could run into memory overflow

    @staticmethod
    def add_to_queue(src_path: str) -> None:
        if ImageQueue.image_queue.full():
            print("Queue is full, cannot add more images")
            return
        try:
            ImageQueue.image_queue.put_nowait(src_path)
            print("Image added to queue: %s %s" % (ImageQueue.get_num_images_in_queue(), src_path))
        except Exception as e:
            print("Exception occured while adding image: %s" % e)
    
    @staticmethod
    def get_from_queue() -> str:
        if ImageQueue.image_queue.empty():
            print("Queue is empty, cannot get an image")
            return
        try:
            ImageQueue.image_queue.get_nowait()
        except Exception as e:
            print("Exception occured while getting an image: %s" % e)
    
    @staticmethod
    def get_num_images_in_queue() -> int:
        return ImageQueue.image_queue.qsize()