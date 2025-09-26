class Timer():
    def __init__(self):
        self.seconds = 0

    def reset(self):
        self.seconds = 0

    def tick(self):
        self.seconds += 1

