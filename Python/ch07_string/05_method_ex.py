email_input = input('이메일 주소를 입력하세요 : ')

valid = email_input.count('@')==1 and email_input.count('.')==1 # @와 .이 한 개씩만
valid = valid and email_input.find('@')<email_input.find('.')-1 # @와 .순서 및 사이의 문자존재
valid = valid and email_input.find('@')>0 and email_input.find('.')<len(email_input)-1 # 양 끝에 문자 존재

if valid:
    print('이메일 형식이 맞습니다.')
else:
    print('이메일 형식이 아닙니다.')
print('입력한 이메일 : ', email_input)