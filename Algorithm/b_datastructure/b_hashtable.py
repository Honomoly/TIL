class Node:
    def __init__(self, key:str, data):
        self.key = key
        self.data = data
        self.next = None
    
    def __eq__(self, other): # 등호관계는 키값으로 비교
        return self.key == other.key
    
    def __str__(self):
        return "{key=" + self.key + ", data=" + self.data + ", next=" + str(self.next) + "}"
    
    def __hash__(self): # 데이터를 해시값으로 변환
        return 31*sum([ord(s) for s in self.key])

class HashTable:
    def __init__(self, length=30): 
        self.table_length = length
        self.table = [None for _ in range(self.table_length)]
        self.length = 0
    
    def __iter__(self):
        return HashTable.Iterator(self)
    
    def __str__(self):
        string = "["
        for hs in self.table:
            if hs is not None:
                nd = hs
                while nd:
                    string += "{key="+nd.key+", value="+nd.data+"}, "
                    nd = nd.next
        if string == "[":
            string += "]"
        else:
            string = string[:-2]+"]"
        return string
    
    def hash(self, node):
        # print(hash(node)%self.table_length) # 해시충돌 테스트용 표시 코드
        return hash(node)%self.table_length
    
    def add(self, key:str, data):
        self.__comm_context(key, data, 1)
    
    def __setitem__(self, key:str, data):
        self.__comm_context(key, data, 2)
    
    def __comm_context(self, key:str, data, aors):
        if type(key) is not str:
            raise TypeError("Not suitable type")
        node = Node(key, data)
        index = self.hash(node)
        link = self.table[index]
        if link is None:
            if aors == 1:
                self.table[index] = node # add 에서만 가능
                self.length += 1
            else:
                print(f"SET ERROR : Key '{node.key}' does not exist!")
            return
        else:
            while link:
                if link == node: # 키가 동일한 경우
                    if aors == 2:
                        link.data = data # set 에서만 가능
                    else:
                        print(f"ADD ERROR : Key '{link.key}' already exist!")
                    return
                prev = link
                link = link.next
            if aors == 1:
                prev.next = node # add 에서만 가능
                self.length += 1
            else:
                print(f"SET ERROR : Key '{node.key}' does not exist!")
    
    def __getitem__(self, key:str):
        hscode = self.hash(Node(key, None))
        for hs in self.table:
            if hs is None:
                continue
            elif self.hash(hs) == hscode:
                nd = hs
                while nd:
                    if nd.key == key:
                        return nd.data
                    nd = nd.next
    
    def __delitem__(self, key:str):
        hscode = self.hash(Node(key, None))
        for i in range(len(self.table)):
            hs = self.table[i]
            if hs is None:
                continue
            elif self.hash(hs) == hscode:
                if hs.key == key:
                    self.table[i] = hs.next # 이 설정을 위해 for i in ~ 형식을 사용
                    return
                else:
                    while hs.next:
                        prev = hs
                        hs = hs.next
                        if hs.key == key:
                            prev.next = hs.next
                            return
    
    class Iterator:
        def __init__(self, hashtable):
            self.table = hashtable.table
            self.table_size = len(self.table)
            self.length = hashtable.length
            self.p = 0
            self.link = self.table[self.p]
            self.iter_cnt = 0
        
        # 이거 필요 없는거 아녀?
        # def __iter__(self):
        #     return self
        
        def __next__(self):
            if self.iter_cnt >= self.length:
                raise StopIteration
            
            while self.link is None:
                self.p += 1
                self.link = self.table[self.p]
            
            result = self.link.data

            if self.link.next is None:
                self.p +=1
                if self.p < self.table_size:
                    self.link = self.table[self.p]
            else:
                self.link = self.link.next

            self.iter_cnt += 1
            return result