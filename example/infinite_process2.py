import time

class InfiniteProcess2:
    def __init__(self):
        pass

    def infinite_loop(self):
        while True:
            print("InfProcess 2", flush=True)
            time.sleep(2)