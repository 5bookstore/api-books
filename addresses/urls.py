from django.urls import path
from . import views

urlpatterns = [
    path("adress/", views.AdressListCreate.as_view()),
    path("adress/<pk>/", views.AdressDetail.as_view()),
]
