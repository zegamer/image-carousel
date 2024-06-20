from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from time import sleep
from .queue_handler import ImageQueue
from .utils import ImageCheck

class _FileHandler(FileSystemEventHandler):

    '''
    Overriding on_create from FileSystemEventHandler
    '''
    @staticmethod
    def on_created(event: FileSystemEvent) -> None:
        src = event.src_path
        if ImageCheck.is_image_ext_valid(src):
            ImageQueue.add_to_queue(src)

    # @staticmethod
    # def on_deleted(event: FileSystemEvent) -> None:
    #     print("File deleted  - %s" % event)


class Listener(_FileHandler):
    def __init__(self, directory = ".", interval = 10):
        self.directory = directory
        self._handler = _FileHandler()
        self.observer = Observer()
        self.interval = interval

    def run(self):
        self.observer.schedule(self._handler, self.directory, recursive=False)
        print("Starting listener")
        self.observer.start()
        try:
            while True:
                sleep(self.interval)
        except:
            self.observer.stop()
        self.observer.join()

