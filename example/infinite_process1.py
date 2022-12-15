import time

class InfiniteProcess1:
    def __init__(self):
        pass

    def infinite_loop(self):
        while True:
            print("InfProcess 1", flush=True)
            time.sleep(2)