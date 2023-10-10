from django.shortcuts import render

# Create your views here.

# urls.py에서 요청을 받고 처리하는 함수를 모아둔다
def index(request):
    return render(request, "first_app/index.html")

def show_img(request):
    # dict 형식
    # member = {}
    # member['name'] = '홍길동'
    # member['age'] = 20
    # return render(request, "first_app/img.html", {'member': member})
    # render(request, "페이지", {데이터})

    members = [
        {'name': '홍길동', 'age': 30},
        {'name': '이몽룡', 'age': 23},
        {'name': '성춘향', 'age': 21}
    ]
    return render(request, "first_app/img.html", {'members': members})

def data_form(request):
    # 전송된 데이터 받기
    if request.method == "POST":
        print(request.POST)
    return render(request, "first_app/data_form.html")