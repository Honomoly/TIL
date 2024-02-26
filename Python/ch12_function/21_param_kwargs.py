# 가변길이 매개변수 (Variadic Keyword Arguments : **kwargs)
# 딕셔너리 형식을 따름

def show_keyword(**kwargs):
    for key in kwargs.keys():
        print(key, end=' ')
    print('\n')
    for value in kwargs.values():
        print(value, end=' ')
    print('\n')
    for item in kwargs.items():
        print(item)
    print('\n')

show_keyword(
    id='abcd',
    name='kim',
    phone='010-1234-5678',
    address='서울'
)

show_keyword(
    id='sky',
    name='lee',
    phone='010-1111-1111',
    address='제주'
)