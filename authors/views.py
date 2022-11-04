from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from .permissions import IsAdminOrReadyOnly
from .serializers import AuthorSerializer
from .models import Author




# Create your views here.
class AuthorView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadyOnly]

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class DetailAuthorView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminOrReadyOnly]

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()



    


