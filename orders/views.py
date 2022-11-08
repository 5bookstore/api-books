from rest_framework.views import Request, Response, status, APIView
from django.core.exceptions import ValidationError
from .serializers import OrderSerializer
from .models import Order
from books.models import Book
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

class OrderListAndCreateViews(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Order.objects.all()

    serializer_class = OrderSerializer

    lookup_url_kwarg = 'book_id'

    def post(self, request: Request, *args, **kwargs) -> Response:
        
        book_id = kwargs[self.lookup_url_kwarg]

        try:
            book = Book.objects.filter(id=book_id)
        except ValidationError:
            return Response({'datail': 'Book not found'}, status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, book=book)

        return Response(serializer.data)


class OrderRetriveUpdateDestroyViews(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()

    serializer_class = OrderSerializer
 