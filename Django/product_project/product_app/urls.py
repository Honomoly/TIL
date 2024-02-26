from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("product_list/", views.product_list, name="product_list"),
    path("product_detail/<str:prd_no>/", views.product_detail, name="product_detail"),
    # <str:prd_no> : 클라이언트로부터 받아 views까지 전달하는 매개변수 역할을 한다
    path("product_insert/", views.product_insert, name="product_insert"),
    path("product_update/<str:prd_no>/", views.product_update, name="product_update"),
    path("product_delete/<str:prd_no>/", views.product_delete, name="product_delete"),
    path('product_search_form/', views.product_search_form, name='product_search_form'),
    path('product_search/', views.product_search, name='product_search'),
    # Ajax용 요청 url
    path('product_get_data/', views.get_data, name='get_data'),
    path('product_ajax_test/', views.ajax_test, name='ajax_test'),
    path('product_search_form2/', views.product_search_form2, name='product_search_form2'),
    path('product_search2/', views.product_search2, name='product_search2'),
    path('product_search_form3/', views.product_search_form3, name='product_search_form3'),
    path('product_search3/', views.product_search3, name='product_search3'),
]