from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.authentication import TokenAuthentication
from .permissions import isUserOrAdmin
from rest_framework.response import Response
import ipdb
from django.shortcuts import get_object_or_404
from books.models import Book



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
        for elem in request.data:
            object_book = Book.objects.get(id=elem["books"])
            serializer = OrderSerializer(data=elem,context={"user":request.user})
            serializer.is_valid(raise_exception=True)
            serializer.save(books=object_book)
        return Response(serializer.data)

