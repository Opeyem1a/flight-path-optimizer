class PriorityQueue:
    def __init__(self):
        self.list = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, state):
        self.list.insert(0, state)
        self.size += 1

    def dequeue(self):
        self.list.pop()
        self.size -= 1
