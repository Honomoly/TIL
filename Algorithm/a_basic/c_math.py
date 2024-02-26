def is_prime(num):
    for i in range(2, num):
        if num%i == 0:
            return False;
        elif i**2>num:
            break;
    return True

def gcd1(a, b):
    min = a
    if min>b:
        min = b
    for i in range(min, 0, -1):
        if a%i==0 and b%i==0:
            return i

def gcd2(a, b):
    if a>b:
        b, a = a, b
    while True:
        a, b = b%a, a
        if a==0:
            break
    return b

def lcm(a, b):
    return a*b//gcd2(a, b)

def factorial1(n):
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

def factorial2(n):
    if n<0:
        return -1
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial2(n-1)

def fibonacci1(n):
    if n<0:
        return -1
    elif (n==1 or n==2):
        return 1
    else:
        a, b = 1, 1
        for i in range(n-2):
            a, b = b, a+b
        return b

def fibonacci2(n):
    if n<0:
        return -1
    elif (n==1 or n==2):
        return 1
    else:
        return fibonacci2(n-1) + fibonacci2(n-2)