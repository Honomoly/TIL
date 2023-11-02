class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def enqueue(self, data):
        if self.front is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
        self.length += 1
    
    def dequeue(self):
        if self.front is None:
            return None
        else:
            data = self.front.data
            self.front = self.front.next
            if self.length == 1:
                self.rear = None
            self.length -= 1
            return data
    
    def is_empty(self):
        return self.front is None