class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.pointer = 0

    def append(self, item):
        
        if self.pointer >= 5:
            self.pointer = 0

        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            if len(self.data) >= self.capacity:
                self.data.remove(self.data[self.pointer])
                self.data.insert(self.pointer, item)
                self.pointer += 1
       
    def get(self):
        return self.data


