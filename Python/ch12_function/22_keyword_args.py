# 키워드 인수
def student_info(name, age, gender):
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student

print(student_info(name='kim', age='26', gender='여'))
print(student_info('lee', gender='남', age=30)) # 순서에 상관없이 알아서 키워드에 해당하는 매개변수로 들어감