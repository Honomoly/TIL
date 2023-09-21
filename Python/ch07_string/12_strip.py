hello = '    hello    '

print(hello)
print(hello.strip())
print(hello.lstrip())
print(hello.rstrip())

id = 'sun'
input_id = ' sun'
if id == input_id.strip():
    print('성공')
else:
    print('실패')