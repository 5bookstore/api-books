from .models import Categories

from rest_framework.authentication import TokenAuthentication

from cards.permissions import IsAdminOrUser, HasObjectPermissionOrIsAdmin

from .serializers import CategoriesSerializer
from rest_framework import generics

class CategoriesListAndCreateViews(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    
    permission_classes = [IsAdminOrUser]
    queryset = Categories.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CategoriesSerializer
        return CategoriesSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CategoriesPatchDestroyViews(generics.UpdateAPIView, generics.DestroyAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [HasObjectPermissionOrIsAdmin]

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
