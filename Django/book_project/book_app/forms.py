from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'book_no',
            'book_name',
            'book_author',
            'book_price',
            'book_date',
            'book_stock',
            'pub_no'
        )
        labels = {
            'book_no': '도서번호',
            'book_name': '도서명',
            'book_author': '저자',
            'book_price': '가격',
            'book_date': '출판일자',
            'book_stock': '재고수량',
            'pub_no': '출판사번호'
        }