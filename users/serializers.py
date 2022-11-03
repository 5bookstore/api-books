from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password":{"write_only":True},"groups":{"write_only":True},"user_permissions":{"write_only":True},"last_login":{"write_only":True},"is_staff":{"write_only":True}}
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()