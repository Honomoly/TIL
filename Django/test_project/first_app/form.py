from django import forms
# Django의 내장 클래스

class DataForm(forms.Form): # 폼 상속
    name = forms.CharField(max_length=10, label="name2")
    age = forms.IntegerField(label="age2")
