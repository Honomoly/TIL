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
    
    def __str__(self):
        if self.front is None:
            return "QueueClass[]"
        string = "QueueClass["
        link = self.front
        while link:
            string += str(link.data) + ", "
            link = link.next
        string = string[:-2] + "]"
        return string

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

class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        if self.top is None:
            return "StackClass[]"
        link = self.top
        result = "StackClass[" + str(link.data) + ", "
        while link.next:
            link = link.next
            result += str(link.data) + ", "
        result = result[:-2] + "]"
        return result
    
    def push(self, data):
        node = Node(data)

        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        
    def pop(self):
        if self.top is None:
            return None
        res = self.top.data
        self.top = self.top.next
        return res
    
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None