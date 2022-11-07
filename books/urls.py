from books.views import BookListAndPostViews, BookUpdateAndDestroyViews

from django.urls import path

urlpatterns = [
    path("books/", BookListAndPostViews.as_view()),
    path("books/<pk>", BookUpdateAndDestroyViews.as_view()),
]
