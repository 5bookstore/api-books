from rest_framework import serializers

from .models import User
from addresses.serializers import SerializerAddress,Address

class UserSerializer(serializers.ModelSerializer):
    address = SerializerAddress()
    
    class Meta:
        model = User
        fields = ["id","username","first_name","last_name","email","is_active","cpf","address","date_joined"]
        extra_kwargs = {"password":{"write_only":True},"groups":{"write_only":True},"user_permissions":{"write_only":True},"last_login":{"write_only":True},"is_staff":{"write_only":True}}
    
    def create(self, validated_data):
        addressData = validated_data.pop("address")
        addressCreate = Address.objects.create(**addressData)
        return User.objects.create_user(**validated_data,address = addressCreate)
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()