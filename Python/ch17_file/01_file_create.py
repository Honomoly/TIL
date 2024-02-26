
# 현재 폴더 경로 확인
import os
print(os.getcwd())

# 터미널에서 이동
# cd 폴더명 : 하위에 있는 해당폴더으로 이동
# cd .. : 상위 폴더로 이동

f = open('ch17_file/file1.txt', 'w') # 터미널의 디랙터리 기준으로 파일생성
f.close()

f = open('/Users/jangseungheon/pythonWorkSpace/ch17_file/file2.txt', 'w') # 전체경로 지정으로도 생성 사능
f.close()

# 경로명에 역슬래시(\) 사용하면 오류!
# 사용할거면 두 개로! (\\)

# close() 사용 안할 시 나중에 다시 열 경우 오류가 발생할 수 있다