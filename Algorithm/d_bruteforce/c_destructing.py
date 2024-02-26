class User:
    def __init__(self, name, age, job, hobby):
        self.name = name
        self.age = age
        self.job = job
        self.hobby = hobby
    
    def __str__(self):
        return f"name={self.name}, age={self.age}, job={self.job}, hobby={self.hobby}"

def destructing():
    a, b, c = [1, 2, 3]
    print(a, b, c)

    a, b = [1, [a, b]]
    print(a, b)

    # 구조 분해 할당
    a, [b, c] = [1, [2, 3]]
    print(a, b, c)
    
    a, *mid, c = [1, 2, 3, 4, 5, 6]
    print(a, mid, c)

    hmd = {
        'nickname' : '하명도',
        'info' : {'age' : 20, 'job' : 'lecture'},
        'hobby' : ['축구', '농구', '배구'],
        'reg_data' : '2023-11-04',
        'next' : '/user/password'
    }
    name, [age, job], hobby = hmd['nickname'], hmd['info'].values(), hmd['hobby']
    HMD = User(name, age, job, hobby)
    print(HMD)

# destructing()

def expon(A, B):
    lst = []
    Quo = B
    while Quo>1:
        Quo, Rem = Quo//2, Quo%2
        lst.append(Rem)
    rlt = A
    for i in range(len(lst)):
        Rem = lst[len(lst)-1-i]
        if Rem == 0:
            rlt *= rlt
        else:
            rlt *= rlt*A
    return rlt

# print(expon(2, 13))