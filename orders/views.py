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

    def create(self, request, *args, **kwargs):
        serializer = OrderSerializer(
            data=request.data,
            context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

