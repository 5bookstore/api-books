from cards.permissions import IsAdminOrUser, HasObjectPermissionOrIsAdmin
from .serializers import BookSerualizer
from .models import Book

from rest_framework import generics

from rest_framework.authentication import TokenAuthentication


class BookListAndPostViews(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    
    permission_classes = [IsAdminOrUser]
    queryset = Book.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return BookSerualizer
        return BookSerualizer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BookUpdateAndDestroyViews(generics.UpdateAPIView, generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [HasObjectPermissionOrIsAdmin]

    queryset = Book.objects.all()
    serializer_class = BookSerualizer
