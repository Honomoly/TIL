from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.board_form, name="board_form"),
]