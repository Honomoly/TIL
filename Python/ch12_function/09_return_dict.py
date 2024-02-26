def get_info() :
    dict = {}
    dict['이름'] = input('이름 입력 : ')
    dict['나이'] = int(input('나이 입력 : '))
    return dict

info = get_info()

print(info)
print(type(info))