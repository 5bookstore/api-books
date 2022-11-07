from cards.permissions import IsAdminOrUser, HasObjectPermissionOrIsAdmin
from .serializers import BookSerializer, EbookSerializer
from .models import Book
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from authors.models import Author
import ipdb


class BookListAndPostViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET" or self.request.data["type"] == "Book":
            return BookSerializer
        return EbookSerializer

    def perform_create(self, serializer):

        autor_data = self.request.data.pop("author")
        author_exist = get_object_or_404(Author, id=autor_data)

        serializer.save(author=author_exist)


class BookUpdateAndDestroyViews(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [HasObjectPermissionOrIsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
