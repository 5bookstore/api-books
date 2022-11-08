from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isUserOrAdmin
from django.shortcuts import get_object_or_404
from books.models import Book
from rest_framework import status
from rest_framework.response import Response
import ipdb


class OrderListAndCreateViews(generics.ListCreateAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [isUserOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    """
        FAZER GET DE QUERYSET - FILTRAGEM POR USUARIO 
    def get_queryset(self):
        return super().get_queryset()
    """

    def create(self, request, *args, **kwargs):
        # ipdb.set_trace()
        # print("1" * 1)
        object_book = get_object_or_404(Book, id=request.data["books"])
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(books=object_book)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
