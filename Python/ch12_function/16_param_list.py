# 리스트를 매개변수로 받는 경우 얕은 복사로 진행한다
# 그러므로 함수내에서 리스트가 수정되면 원본도 수정된다
def show_names(names):
    names.append('jang') # 이러면 매개변수로 들어간 리스트의 원본도 변경
    print(names)

names_list = ['kim', 'lee', 'park']

print(names_list)
show_names(names_list)
print(names_list)

print()

# 깊은 복사 방식 추가
def show_names2(names):
    names = list(names)
    names.append('gang')
    print(names)

print(names_list)
show_names2(names_list)
print(names_list)