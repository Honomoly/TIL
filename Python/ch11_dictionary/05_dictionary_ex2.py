dictionary = {}

while True:
    input_word = input('영어 단어 등록(종료는 quit) : ')
    if input_word in dictionary.keys():
        print(input_word+'는 이미 등록된 단어입니다.\n')
    elif input_word == 'quit':
        break
    else:
        input_mean = input(input_word+'의 뜻 입력(종료는 quit) : ')
        print()
        if input_mean == 'quit':
            break
        dictionary[input_word] = input_mean

print()

while True:
    input_search = input('검색할 단어 입력(종료는 quit) : ')

    if input_search == 'quit':
        break
    elif input_search not in dictionary.keys():
        print(input_search+'는 사전에 없는 단어입니다.\n')
    else:
        print(input_search+'의 뜻은 '+dictionary[input_search]+'입니다.\n')

print('종료합니다')
