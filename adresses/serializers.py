from rest_framework import serializers
from .models import Adress


class SerializerAdress(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = [
            "street_name",
            "district",
            "number",
            "zip_code",
            "city",
            "state",
            "adress_complement",
        ]

    def create(self, validated_data):
        return Adress.objects.create(**validated_data)
