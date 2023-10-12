from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.http import JsonResponse
from django.core import serializers
from .models import *
from .forms import *
import json

# Create your views here.
def index(request):
    return render(request, "book_app/index.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_app/book_list.html", {'books': books})

def book_insert(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/book/list/")
    else:
        form = BookForm()
        return render(request, "book_app/book_insert.html", {'form':form})
    
def book_update(request, book_no):
    book = get_object_or_404(Book, pk=book_no)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("/book/list/")
    else:
        form = BookForm(instance=book)
        return render(request, "book_app/book_insert.html", {'form':form})
    
def book_delete(request, book_no):
    book = get_object_or_404(Book, pk=book_no)
    book.delete()
    return redirect("/book/list/")

def book_detail(request, book_no):
    book = get_object_or_404(Book, pk=book_no)
    return render(request, "book_app/book_detail.html", {'book':book})

def book_search_form(request):
    return render(request, "book_app/book_search.html")

def book_search(request):
    if request.method == 'POST':
        type = request.POST['type']
        keyword = request.POST['keyword']
        if type == 'book_name':
            book_list = Book.objects.filter(Q(book_name__contains=keyword))
        else:
            book_list = Book.objects.filter(Q(book_author__contains=keyword))
        book_list_json = json.loads(serializers.serialize('json', book_list, ensure_ascii=False))

        # 출판사 이름을 담은 json파일을 따로 만들어서 같이 보내기
        pubs = []
        for book in book_list_json:
            pubs.append(Publisher.objects.get(pk=book['fields']['pub_no']))
        print(pubs)
        pubs_json = json.loads(serializers.serialize('json', pubs, ensure_ascii=False))
        for pub in pubs_json:
            print(pub)

        return JsonResponse({'reload_all':False, 'book_list_json':book_list_json, 'pubs_json':pubs_json})