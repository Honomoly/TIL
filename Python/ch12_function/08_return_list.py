def get_names():
    name1 = input('이름 입력 : ')
    name2 = input('이름 입력 : ')
    name3 = input('이름 입력 : ')
    return [name1, name2, name3]

names = get_names()

print(names)
print(type(names))