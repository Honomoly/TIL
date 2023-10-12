from django.shortcuts import render, redirect
from first_app.form import DataForm

# Create your views here.

# urls.py에서 요청을 받고 처리하는 함수를 모아둔다
def index(request):
    return render(request, "first_app/index.html")

def show_img(request):
    # dict 형식으로 입력
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
    # 첫 def문 실행에서 request는 GET 형식으로 생성된다
    # 입력된 데이터가 제출되면 request는 POST 방식으로 바뀌어서 def문이 재실행 된다
    # 그러므로 if문이 실행된다
    if request.method == "POST":
        print(request.POST)
    return render(request, "first_app/data_form.html")

def data_form2(request):
    form = DataForm(request.POST)
    print(request)
    print(request.POST)
    print(request.method)
    if request.method == "POST":
        if form.is_valid():
            name = request.POST.get('name', None)
            age = request.POST.get('age', None)
            print(name)
            print(age)
            # index 페이지로 포워딩
            return redirect('/')
    return render(request, "first_app/data_form2.html", {'form':form})

