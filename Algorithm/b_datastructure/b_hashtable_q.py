from b_hashtable import *

def q1(text):
    table = HashTable()
    max = 0
    for l in text:
        if table[l] is None:
            table.add(l, 1)
        else:
            table[l] += 1
        if table[l] > max:
            max = table[l]
    
    ls = []
    for l in text:
        if table[l] == max and l not in ls:
            ls.append(l)
    return ls