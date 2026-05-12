class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if self.data:
            return self.data.pop()

    def is_empty(self):
        return len(self.data) == 0