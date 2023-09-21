nums = [1, 2, 3, 4, 5]

x = [n for n in nums] # 마치 집합같다!
print(x)

x = [n**2 for n in nums]
print(x)

x = [n for n in nums if n % 2 == 0] # Warning! if문이 for 앞에 오면 오류남
print(x)

x = [n*10 if n % 2 == 0 else n*100 for n in nums] # 근데 if~else는 또 for 앞에 와야함
print(x)