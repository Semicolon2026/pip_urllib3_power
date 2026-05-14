class Retry:
    def __init__(self, total=3):
        self.total = total

    def increment(self):
        if self.total <= 0:
            raise Exception("Max retries exceeded")
        self.total -= 1
