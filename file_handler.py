from watchdog.events import FileSystemEvent, FileSystemEventHandler
from queue_handler import ImageQueue
from utils import ImageCheck

class FileHandler(FileSystemEventHandler):

    @staticmethod
    def on_created(event: FileSystemEvent) -> None:
        # print("File created  - %s" % event.src_path)
        if ImageCheck.is_image_ext_valid(event.src_path):
            # File added to queue
            print("File added to queue")
            ImageQueue.add_to_queue(event.src_path)

    @staticmethod
    def on_deleted(event: FileSystemEvent) -> None:
        print("File deleted  - %s" % event)