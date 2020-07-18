pointer = 0

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        global pointer
        
        if pointer >= 5:
            pointer = 0

        if len(self.data) < self.capacity:
            self.data.append(item)
        else:
            if len(self.data) >= self.capacity:
                self.data.remove(self.data[pointer])
                self.data.insert(pointer, item)
                pointer += 1
       
    def get(self):
        return self.data

