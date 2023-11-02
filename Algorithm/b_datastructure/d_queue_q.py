from d_queue import *

def q1(num):
    qu = Queue()
    for i in range(1, num+1):
        qu.enqueue(i)
    while True:
        print(qu.dequeue(), end=" ")
        if qu.length == 1:
            break
        qu.enqueue(qu.dequeue())
        if qu.length == 1:
            break
    print()
    return qu.dequeue()

def q2(num, kth):
    qu = Queue()
    for i in range(1, num+1):
        qu.enqueue(i)
    while qu.length>1:
        for i in range(kth-1):
            qu.enqueue(qu.dequeue())
        print(qu.dequeue(), end=" ")
    print()
    return qu.dequeue()