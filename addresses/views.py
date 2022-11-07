from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import Request, Response, status, APIView
from .serializers import Address, SerializerAddress
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly


# class AdressListCreate(generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Address.objects.all()
#     serializer_class = SerializerAddress

#     def perform_create(self, serializer):
#         user = self.request.user
#         serializer.save(user=user)


class AdressDetail(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Address.objects
    serializer_class = SerializerAddress
