from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from .models import Product
from .forms import ProductForm
import json

# Create your views here.
def index(request):
    return render(request, "product_app/index.html")

# 전테 상품 조회
def product_list(request):
    # mosels.py로 연결된 DB에서 가져오기
    products = Product.objects.all()
    return render(request, "product_app/product_list.html", {'products': products})

# 상세 상품 조회
def product_detail(request, prd_no):
    # prd_no에 해당하는 상품 정보 가져오기
    # get_object_or_404()메소드 사용
    product = get_object_or_404(Product, pk=prd_no)
    return render(request, "product_app/product_detail.html", {'product': product})

# 상품 등록
def product_insert(request):
    # (1) 데이터가 입력되었는지 확인 (요청이 POST형식인지 확인)
    if request.method == "POST":
        # (2) 입력받은 데이터를 클래스를 통하여 저장
        form = ProductForm(request.POST)
        # (3) Django의 기본 기능인 is_valid()메소드로 유효성 검사
        if form.is_valid():
            # (4) 추가적인 작업이 존재한다면 완전히 저장을 하지 않고 작업을 진행한다(여기서는 없다)
            product = form.save(commit=False)
            # (5) 작업이 끝나면 최종적으로 DB에 저장한다
            product.save()
            # (6) 저장이 끝났다면 상품정보 조회로 포워딩 한다
            return redirect("/product_list/")
    else:
        form = ProductForm()
    # (7) 데이터가 입력된 것이 아니면(POST가 아니면) 입력하는 폼 그대로 출력
    return render(request, 'product_app/product_form.html', {'form':form})

# 상품정보 수정
def product_update(request, prd_no):
    # (1) prd_no에 해당하는 정보를 가져온다
    product = get_object_or_404(Product, pk=prd_no)
    # (2) 요청이 POST형식인지 확인한다
    if request.method == "POST":
        # (3) 입력 받아온 내용을 form 변수에 저장
        form = ProductForm(request.POST, instance=product)
        # (4) Django의 기본 기능인 is_valid()메소드로 유효성 검사
        if form.is_valid():
            # (5) 추가적인 작업이 존재한다면 완전히 저장을 하지 않고 작업을 진행한다(여기서는 없다)
            product = form.save(commit=False)
            # (6) 작업이 끝나면 최종적으로 DB에 저장한다
            product.save()
            # (7) 저장이 끝났다면 상품정보 조회로 포워딩 한다
            return redirect("/product_list/")
    else:
        # (1-2) 처음에는 prd_no에 해당하는 폼을 그대로 반영하여 보여준다
        form = ProductForm(instance=product)
    # (8) 데이터가 입력된 것이 아니면(POST가 아님) (1)에서 찾아온 수정할 정보 그대로 출력
    return render(request, 'product_app/product_update.html', {'form':form})

# 상품 삭제
def product_delete(request, prd_no):
    # request는 받아봤자 호출할 페이지가 없어 쓸 곳이 없다
    # (1) prd_no에 해당하는 상품 호출
    product = get_object_or_404(Product, pk=prd_no)
    # (2) 상품 삭제
    product.delete()
    # (3) 상품목록으로 이동
    return redirect("/product_list/")

# 상품 검색
def product_search_form(request):
    return render(request, "product_app/product_search_form.html")

def product_search(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']
        print(type, keyword) # 터미널에 테스트 출력

        # filter()메소드및 Q 객체 사용
        if type == 'prd_name':
            prd_list = Product.objects.filter(Q(prd_name__contains=keyword))
        else:
            prd_list = Product.objects.filter(Q(prd_maker__contains=keyword))
        return render(request, "product_app/product_search_form.html", {'prd_list':prd_list})
    
# Ajax 연습
def ajax_test(request):
    return render(request, "product_app/ajax_test.html")

def get_data(request):
    # 데이터 전송
    data = {'input_data': 'None'}
    if request.method == 'POST':
        data['input_data'] = request.POST['test_input']
    return JsonResponse(data)

# Ajax 검색
def product_search_form2(request):
    return render(request, "product_app/product_search_form2.html")

def product_search2(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']
        if type == 'prd_name':
            prd_list = Product.objects.filter(Q(prd_name__contains=keyword))
        else:
            prd_list = Product.objects.filter(Q(prd_maker__contains=keyword))

        # 여기서 쿼리 데이터셋인 prd_list를 json 타입으로 변경한다
        prd_list_json = json.loads(serializers.serialize('json', prd_list, ensure_ascii=False))

        return JsonResponse({'reload_all': False, 'prd_list_json': prd_list_json})
    
def product_search_form3(request):
    return render(request, "product_app/product_search_form3.html")

def product_search3(request):
    if request.method == "POST":
        type = request.POST['type']
        keyword = request.POST['keyword']
        if type == 'prd_name':
            prd_list = Product.objects.filter(Q(prd_name__contains=keyword))
        else:
            prd_list = Product.objects.filter(Q(prd_maker__contains=keyword))

        return render(request, "product_app/product_search_form3_0.html", {'prd_list':prd_list})