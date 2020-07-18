class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # take the current list and reverse the order.
        # remove the head and
        # prev = self.head.get_next(self)
        # newList = []

        # if node:
        #     newList.append(node.value)
        #     return self.reverse_list(node, prev)


        if self.head is None: 
            return self.head 
  
        # Reverse the rest list 
        rest = self.reverse_list(self.head.get_next(), prev) 
  
        # Put first element at the end 
        self.head.next.next = self.head 
        self.head.next = None
  
        # Fix the header pointer 
        return rest 