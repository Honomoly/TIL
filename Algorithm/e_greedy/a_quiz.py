from Algorithm.tools import Stack

def q1(charge):
    c500, charge = charge//500, charge%500
    c100, charge = charge//100, charge%100
    c50, charge = charge//50, charge%50
    c10, charge = charge//10, charge%10
    return {'500' : c500, '100' : c100, '50' : c50, '10' : c10, 'remain' : charge}

# print(q1(3465))

def q2(meeting_table):
    ls = [0]
    rlt = []
    do_plus = True
    idx = 0
    while True:
        if do_plus:
            stop = True
            for j in range(idx, len(meeting_table)):
                if meeting_table[ls[-1]]['end'] <= meeting_table[j]['start']:
                    ls.append(j)
                    stop = False
                    idx = 0
                    break
        if stop:
            print(ls)
            if len(rlt) < len(ls):
                rlt = [_+1 for _ in ls]
            idx = ls[-1]+1
            if idx >= len(meeting_table):
                do_plus = False
            del ls[-1]
            if len(ls) <= 0:
                if idx < len(meeting_table):
                    ls.append(idx)
                    idx = 0
                else:
                    break
            do_plus = True
    return rlt

meetings = [
    {'idx':1,'start':1, 'end':10},
    {'idx':2,'start':5, 'end':6},
    {'idx':3,'start':13,'end':15},
    {'idx':4,'start':14,'end':17},
    {'idx':5,'start':8, 'end':14},
    {'idx':6,'start':3, 'end':12}
]

print("회의 순서 : ", q2(meetings))