class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# list에 해당하는 유사한 object를 직접 만들어보자
class LinkedList:
    def __init__(self):
        self.head = None # list의 시작 노드에 해당해는 내용(list 전체 내용을 담고 있다)
        self.tail = None # list의 끝 노드에 해당하는 내용(list 끝 내용만을 담고 있다)
        self.length = 0 # list의 길이
        self.now = None
    
    def __len__(self): # 데이터 길이 반환
        return self.length

    def __str__(self): # 데이터 대표값 반환
        string = ""
        nd = self.head
        if nd is None:
            return "[]"
        else:
            while True:
                string += str(nd.data) + ", "
                nd = nd.next
                if nd is None:
                    string = "[" + string[:-2] + "]"
                    break
            return string
    
    # iterable object로 만들기
    def __iter__(self): # iteration 시작시 실행
        self.now = self.head # iteration을 시작할 때마다 시작 노드를 지정(self.head를 건드리지 않기 위함)
        return self # 무조건 자기 자신을 반환한다
    
    def __next__(self): # iteration 수행
        if self.now is None: # 더이상 없으면 끝
            raise StopIteration
        else:
            data = self.now.data 
            self.now = self.now.next # 다음 노드를 지정
            return data # 각 시행마다 반환하는 값 지정
        
    # 연산자 기능도 추가
    def __le__(self, other): # list 길이로 less than or equal을 정의하기
        return self.length <= other.length
    
    # 가장 뒤를 반환하고 삭제
    def pop(self):
        if self.tail is None:
            return None
        else:
            node = self.head
            while node.next: # None이 아닐 때까지 반복
                prev = node
                node = node.next
            data = node.data
            prev.next = None
            self.length -= 1
            return data
        
    # 인덱스로 확인하기
    def __getitem__(self, idx:int):
        if idx<0 or idx>= self.length:
            raise IndexError("Index is out of range")
        else:
            node = self.head
            for i in range(idx):
                node = node.next
            return node.data
    
    def __setitem__(self, idx:int, ipt):
        if idx<0 or idx>= self.length:
            raise IndexError("Index is out of range")
        else:
            node = self.head
            for i in range(idx):
                node = node.next
            node.data = ipt
    
    def __delitem__(self, idx:int):
        if idx<0 or idx>= self.length:
            raise IndexError("Index is out of range")
        else:
            node = self.head
            new_node = self.head
            i = 0
            for i in range(idx):
                prev = node
                node = node.next
            prev.next = node.next
            self.length -= 1
    
    # 추가하는 함수
    def append(self, data):
        node = Node(data) # 입력 노드
        if self.tail is None: # 아무것도 없을 때
            self.head = node # 시작도 입력 노드
            self.tail = node # 끝도 입력 노드
        else:
            self.tail.next = node # 끝에 입력 노드를 추가한다
            self.tail = node # 끝을 입력 노드로 갱신
        self.length += 1
    
    def prepand(self, data):
        node = Node(data) # 입력 노드
        if self.tail is None: # 아무것도 없을 때
            self.head = node # 시작도 입력 노드
            self.tail = node # 끝도 입력 노드
        else:
            node.next = self.head # 입력 노드에 기존 리스트(시작 노드)를 갖다 붙인다
            self.head = node # 그 다음 해당 노드를 시작으로 설정한다
        self.length += 1
    
    def insert(self, idx:int, data):
        if idx<0 or idx>= self.length:
            raise IndexError("Index is out of range")
        else:
            node = self.head
            for i in range(idx):
                prev = node
                node = node.next
            new_node = Node(data)
            new_node.next = node
            prev.next = new_node
            self.length += 1