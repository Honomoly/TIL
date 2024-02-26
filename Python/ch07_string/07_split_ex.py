birth = input('생일 입력 (연/월/일) : ')

birth_split = birth.split('/')
print('당신은 %s년에 태어났고'%birth_split[0])
print('생일은 %s월 %s일 이군요'%(birth_split[1], birth_split[2]))