def max(a, b, c):
    if a>b:
        max = a
    else:
        max = b
    if c>max:
        max = c
    return max

def min(a, b, c):
    if a>b:
        min = b
    else:
        min = a
    if c<min:
        min = c
    return min

def med(a, b, c):
    if a>b:
        l = a
        s = b
    else:
        l = b
        s = a
    
    if c>l:
        med = l
    elif c<s:
        med = s
    else:
        med = c
    return med

print(max(55, 255, 30))
print(min(55, 255, 30))
print(med(55, 255, 30))