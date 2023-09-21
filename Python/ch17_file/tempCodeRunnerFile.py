f1 = open('test2.txt', 'r')
data = f1.read()
print(data)
print(type(data))
print(len(data))
for ch in data:
    print(ord(ch))
f1.close()