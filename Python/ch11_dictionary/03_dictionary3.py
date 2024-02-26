dictionary = {
    'name' : '버섯 불고기 덮밥',
    'type' : '덮밥',
    'ingredient' : ['소고기', '버섯', '양파', '간장', '설탕'],
    'origin' : '한국'
}

dictionary['name'] = '한우 버섯 불고기 덮밥'

print('요리명 : ', dictionary['name'])
print('종류 : ', dictionary['type'])
print('재료 : ', end='')
for ing in dictionary['ingredient']:
    print(ing, end=' ')
print()
print('원산지 : ', dictionary['origin'])


