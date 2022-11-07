from rest_framework.views import Request, Response, status, APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .serializers import ReviewSerializer
from .models import Review
from books.models import Book

from django.core.exceptions import ValidationError


# Create your views here.
class ReviewListAndCreateViews(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    lookup_url_kwarg = 'book_id'

    def post(self, request: Request, *args, **kwargs) -> Response:
        # import ipdb
        # ipdb.set_trace()
        book_id = kwargs[self.lookup_url_kwarg]

        try:
            book = Book.objects.filter(id=book_id)
        except ValidationError:
            return Response({'datail': 'Book not found'}, status.HTTP_404_NOT_FOUND)

        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, book=book)

        return Response(serializer.data)


class ReviewRetriveUpdateDestroyViews(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()

    serializer_class = ReviewSerializer
