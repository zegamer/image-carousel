from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from time import sleep
from file_handler import FileHandler

class Watcher:
    def __init__(self, directory = ".", handler = FileSystemEventHandler()):
        self.directory = directory
        self.handler = handler
        self.observer = Observer()

    def run(self):
        self.observer.schedule(self.handler, self.directory, recursive=True)
        print("Starting listener")
        self.observer.start()
        try:
            while True:
                sleep(10)
        except:
            self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    watch = Watcher(".", FileHandler())
    watch.run()
