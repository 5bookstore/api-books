from rest_framework.views import Request, Response, status, APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import ReviewSerializer, ReviewDetailSerializer
from .models import Review
from books.models import Book
from django.core.exceptions import ValidationError
import ipdb


# Create your views here.
class ReviewListAndCreateViews(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    lookup_url_kwarg = 'book_id'

    def post(self, request: Request, *args, **kwargs) -> Response:
        book_id = request.data['book']

        try:
            book = Book.objects.get(id=book_id)
        except ValidationError:
            return Response(
                {'datail': 'Book not found'},
                status.HTTP_404_NOT_FOUND
            )

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(book=book, user=request.user)

        return Response(serializer.data)


class ReviewRetriveUpdateDestroyViews(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()

    serializer_class = ReviewDetailSerializer

    lookup_url_kwarg = 'review_id'
