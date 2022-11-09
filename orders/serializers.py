from rest_framework import serializers

from orders.models import Order
from books.models import Book
from users.serializers import UserSerializer
from books.serializers import BookSerializer
from books.models import Book
from .utils.fun_util import frete
import ipdb


class OrderSerializer(serializers.ModelSerializer):
    books = serializers.UUIDField()

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
        # extra_kwargs = {
        #     "books": {'write_only': True},
        #     "ammount_items": {'write_only': True},

        # }
        read_only_fields = [
            "id",
            "status",
            "shipping",
            "total_value",
            "user",
        ]

    def create(self, validated_data):
        obj = {
            'user': self.context['user'],
            'data': validated_data
        }

        value_frete = frete(**obj)

        # create = Order.objects.create(**data)
        create.books.add(book)
        return create
