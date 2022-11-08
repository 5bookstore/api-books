from rest_framework import serializers

from orders.models import Order
from books.models import Book
from users.serializers import UserSerializer
from books.serializers import BookSerializer
import ipdb


class OrderSerializer(serializers.ModelSerializer):

    books = BookSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "status",
            "books",
            "shipping",
            "ammount_items",
            "total_value",
            "user",
        ]

        read_only_fields = [
            "status",
            "shipping",
            "ammount_items",
            "total_value",
            "user",
        ]
