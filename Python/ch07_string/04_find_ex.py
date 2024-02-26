cities = '인천 대전 광주 울산 대구 부산'
input_ = input('우리나라 광역시 중 하나 입력 : ')

if cities.find(input_)==-1:
    print('틀렸습니다')
else:
    print('정답입니다')