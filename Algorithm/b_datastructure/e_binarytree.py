from c_stack import Stack
from d_queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.data

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0
    
    def insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            self.length += 1
            return
        link = self.root
        while True:
            if link.data > data:
                if link.left is None:
                    link.left = node
                    self.length += 1
                    break
                link = link.left
            if link.data < data:
                if link.right is None:
                    link.right = node
                    self.length += 1
                    break
                link = link.right
    
    def find(self, data):
        link = self.root
        while True:
            if link is None:
                return False
            if link.data == data:
                return True
            if link.data > data:
                link = link.left
            else:
                link = link.right
    
    def pre_order(self):
        if self.root is not None:
            return self.__pre_order(self.root)
        else:
            return "[]"

    def __pre_order(self, link):
        result = [link.data]
        if link.left is not None:
            result += self.__pre_order(link.left)
        if link.right is not None:
            result += self.__pre_order(link.right)
        return result
    
    def in_order(self):
        if self.root is not None:
            return self.__in_order(self.root)
        else:
            return "[]"
    
    def __in_order(self, link):
        result = []
        if link.left is not None:
            result += self.__in_order(link.left)
        result += [link.data]
        if link.right is not None:
            result += self.__in_order(link.right)
        return result
    
    def post_order(self):
        if self.root is not None:
            return self.__post_order(self.root)
        else:
            return "[]"
    
    def __post_order(self, link):
        result = []
        if link.left is not None:
            result += self.__post_order(link.left)
        if link.right is not None:
            result += self.__post_order(link.right)
        result += [link.data]
        return result

    # 이진트리 깊이 우선 탐색
    def pre_order_with_stack(self):
        stack = Stack()
        link = self.root
        list = []
        while True:
            list.append(link.data)
            if len(list) >= self.length:
                break
            if link.left is not None:
                if link.right is not None:
                    stack.push(link.right)
                link = link.left
                continue
            if link.right is not None:
                link = link.right
                continue
            link = stack.pop()
        return list

    def in_order_with_stack(self):
        stack = Stack()
        link = self.root
        list = []
        while True:
            if len(list) >= self.length:
                break
            if link is not None:
                if link.left is not None:
                    stack.push(link)
                    link = link.left
                    continue
            else:
                link = stack.pop()
            list.append(link.data)
            link = link.right
        return list
    
    def in_order_with_stack2(self):
        stack = Stack()
        link = self.root
        list, sub_list = [], []
        while True:
            if link.left is not None:
                if link.right is not None:
                    stack.push((link.right, link.data, sub_list))
                    sub_list = []
                else:
                    sub_list.insert(0, link.data)
                link = link.left
                continue
            list.append(link.data)
            if link.right is not None:
                link = link.right
                continue
            list += sub_list
            if len(list) >= self.length:
                break
            link, data, sub_list = stack.pop()
            list.append(data)
        return list
    
    def post_order_with_stack(self):
        stack = Stack()
        link = self.root
        list, sub_list = [], []
        while True:
            sub_list.insert(0, link.data)
            if link.left is not None:
                if link.right is not None:
                    stack.push((link.right, sub_list))
                    sub_list = []
                link = link.left
                continue
            if link.right is not None:
                link = link.right
                continue
            list += sub_list
            if len(list) >= self.length:
                break
            link, sub_list = stack.pop()
        return list
    
    def post_order_with_stack2(self):
        stack = Stack()
        link = self.root
        list = []
        while True:
            if len(list) >= self.length:
                break
            if link is None:
                link, dir = stack.pop()
                if dir and link.right is not None:
                    stack.push((link, False))
                    link = link.right
                else:
                    list.append(link.data)
                    link = None
                continue
            if link.left is not None:
                stack.push((link, True))
                link = link.left
                continue
            if link.right is not None:
                stack.push((link, False))
                link = link.right
                continue
            list.append(link.data)
            link = None
        return list
    
    def order_with_stack_fuk(self, typ):
        stack = Stack()
        link = self.root
        stack.push(self.__queue_making(None))
        list = []
        while True:
            state = stack.peek().dequeue()
            if state == 0: # Go to left
                # When first-arrival
                if typ == -1:
                    list.append(link.data)
                if link.left is not None:
                    stack.push(self.__queue_making(link))
                    link = link.left
            elif state == 1: # Go to right
                # When left-search is over
                if typ == 0:
                    list.append(link.data)
                if link.right is not None:
                    stack.push(self.__queue_making(link))
                    link = link.right
            else:
                # When right-search is over
                if typ == 1:
                    list.append(link.data)
                if state is not None:
                    link = state
                    stack.pop()
                else:
                    break
        return list

    def __queue_making(self, link):
        que = Queue()
        for i in [0,1,link]:
            que.enqueue(i)
        return que

    # 이진트리 너비 우선 탐색
    def bfs(self):
        queue = Queue()
        queue.enqueue(self.root)
        level = 0
        while not queue.is_empty():
            print(f"Level {level} : ", end="")
            for i in range(len(queue)):
                lv = queue.dequeue()
                print(lv.data, end=" ")
                if lv.left is not None:
                    queue.enqueue(lv.left)
                if lv.right is not None:
                    queue.enqueue(lv.right)
            level += 1
            print()