import module_main as mm

print(mm.get_name()) # module_main의 main()이 수행되지 않았음

mm.input_name()
print(mm.get_name())

# import 04_module_main2 # 모듈로 import하기 위해서는 파일명이 숫자로 시작하면 안됨

import show_info as si
print(si.age)
print(si.__name__)