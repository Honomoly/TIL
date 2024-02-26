def fibonacci(n):
    if n<0:
        return -1
    elif (n==1 or n==2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibo_dp(n):
    table = [1, 1]
    if n<1:
        return -1
    if n<=2:
        return 1
    for i in range(2, n):
        table.append(table[i-2]+table[i-1])
    return table[-1]

print(fibo_dp(10))