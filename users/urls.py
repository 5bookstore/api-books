from django.urls import path
from .views import ListCreateUserView,LoginView,UpdateActiveView,UpdateUserView
urlpatterns = [
    path("users/",ListCreateUserView.as_view()),
    path("users/<pk>/management",UpdateActiveView.as_view()),
    path("login/",LoginView.as_view()),
    path("users/<pk>",UpdateUserView.as_view())
]