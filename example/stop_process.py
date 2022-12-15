class SimpleProcess:
    def __init__(self, name_: str):
        self.my_name = name_

    def run(self):
        print(f"my name is {self.my_name}")