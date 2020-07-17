class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            if self.size == self.capacity:
                self.size = 0
            self.storage[self.size] = item
            self.size += 1
            
            return self.storage

    def get(self):
        return self.storage