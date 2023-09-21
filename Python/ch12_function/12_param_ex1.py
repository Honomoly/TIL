def get_average(kor, eng, math):
    return (kor+eng+math)/3

input_kor = float(input('국어점수 입력 : '))
input_eng = float(input('영어점수 입력 : '))
input_math = float(input('수학점수 입력 : '))
print('평균 : %.2f'%get_average(input_kor, input_eng, input_math))