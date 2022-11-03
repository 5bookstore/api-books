from rest_framework import serializers

from cards.models import Card


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"