from rest_framework.serializers import ModelSerializer
from .models import Book


class BookSerualizer(ModelSerializer):
    # author = AuthorSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    # order = OrdersSerializer(read_only=True)
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'date_release',
            'book_cover',
            'price',
            'description',
            'publishing_company',
            'language',
            'edition_number',
            'number_pages',
            'country',
            'isbn',
            'type',
            'amount',
            'weigth',
            'format',
            'length',
            'width',
            'diameter',
        ]

        read_only_fields = ['id']
