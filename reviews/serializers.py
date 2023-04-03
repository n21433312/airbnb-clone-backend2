from rest_framework import serializers
from users.serializers import TinyUserSErializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    user = TinyUserSErializer(read_only=True)

    class Meta:
        model = Review
        fields = (
            "user",
            "payload",
            "rating",
        )