
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

a = 9
b = 3
print('%d + %d = %d'%(a, b, add(a, b)))
print('%d - %d = %d'%(a, b, sub(a, b)))
print('%d * %d = %d'%(a, b, mul(a, b)))
print('%d / %d = %d'%(a, b, div(a, b)))