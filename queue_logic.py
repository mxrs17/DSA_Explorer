class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if self.data:
            return self.data.pop(0)

    def is_empty(self):
        return len(self.data) == 0