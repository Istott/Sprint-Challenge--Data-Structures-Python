class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        if len(self.data) < self.capacity:
            self.data.append(item)

        if len(self.data) == self.capacity:
            self.data.remove(self.data[0])
            self.data.append(item)

        if len(self.data) > self.capacity:
            self.data.remove(self.data[0])
            self.data.insert(0, item)
        
        # if len(self.data) > self.capacity:
        #     self.data.remove(self.data[5])
        #     self.data.insert(0, item)
            
    def get(self):
        return self.data

# class RingBufferFull:
#     def __init__(self, n):
#         raise 'you should use RingBuffer'

#     def append(self, item):
#         self.data[self.cur] = item
#         self.cur = (self.cur + 1) % self.capacity
    
#     def get(self):
#         return self.data[self.cur:] + self.data[:self.cur]


