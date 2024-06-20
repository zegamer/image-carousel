from src.listener import Listener

if __name__ == "__main__":
    watch = Listener(directory = ".", interval = 10)
    watch.run()
