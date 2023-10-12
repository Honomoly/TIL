from django.urls import path
from . import views

# path안의 앞에 url을 접근할 형식을 지정해준다
urlpatterns = [
    path("", views.index, name="index"),
    path("img/", views.show_img, name="show_img"),
    path("data_form/", views.data_form, name="data_form"),
    path("data_form2/", views.data_form2, name="data_form2")
]