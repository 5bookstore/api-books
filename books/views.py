from .serializers import BookSerializer, EbookSerializer
from .models import Book
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from django.shortcuts import get_object_or_404
from authors.models import Author
from rest_framework.response import Response
from rest_framework import status


class BookListAndPostViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET" or self.request.data["type"] == "Book":
            return BookSerializer
        return EbookSerializer

    def create(self, request, *args, **kwargs):

        # ipdb.set_trace()
        data = request.data
        if request.data["type"] == "E-book":
            default_ebook_params = {
                "amount": 1,
                "weigth": 1,
                "format": 1,
                "length": 1,
                "width": 1,
                "diameter": 1,
            }
            data.update(**default_ebook_params)

            serializer = BookSerializer(data=data)

            serializer.is_valid(raise_exception=True)

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )

        serializer = BookSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        autor_data = self.request.data.pop("author")
        author_exist = get_object_or_404(Author, id=autor_data)
        serializer.save(author=author_exist)


class BookUpdateAndDestroyViews(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
