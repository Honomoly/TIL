from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'prd_no',
            'prd_name',
            'prd_price',
            'prd_maker',
            'prd_color',
            'ctg_no'
        )
        labels = {
            'prd_no': '상품번호',
            'prd_name': '상품명',
            'prd_price': '가격',
            'prd_maker': '제조사',
            'prd_color': '색상',
            'ctg_no': '카테고리번호'
        }