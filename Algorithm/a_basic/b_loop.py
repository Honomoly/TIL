def q1():
    row = int(input("줄 수 : "))
    col = int(input("칸 수 : "))
    for i in range(row):
        for j in range(col):
            print("*", end="")
        print()

def q2():
    row = int(input("줄 수 : "))
    for i in range(row):
        for j in range(i+1):
            print("*", end="")
        print()

def q3():
    row = int(input("줄 수 : "))
    for i in range(row):
        for j in range(row):
            if i==j:
                print(i+1, end="")
            else:
                print("*", end="")
        print()

def q4():
    row = int(input("줄 수 : "))
    for i in range(row):
        for j in range(i+1):
            if i==j:
                print(i+1, end="")
            else:
                print("*", end="")
        print()

def q5():
    row = int(input("숫자 : "))
    dr = input("방향 : ")
    if dr == "+":
        for i in range(row):
            print(" "*(row-i-1), "*"*(2*i+1))
    else:
        for i in range(row):
            print(" "*(i), "*"*(2*(row-i-1)+1))

def q6():
    row = int(input("숫자 : "))
    for i in range(row):
        print(" "*(row-i-1), "*"*(2*i+1))
    for i in range(1, row):
        print(" "*(i), "*"*(2*(row-i-1)+1))