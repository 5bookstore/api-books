from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"

        extra_kwargs = {"stars": {"min_value": 1, "max_value": 5}}
