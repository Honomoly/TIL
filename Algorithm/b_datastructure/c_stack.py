class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        if self.top is None:
            return "[]"
        link = self.top
        result = "[" + str(link.data) + ", "
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