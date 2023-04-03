from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import TinyUserSErializer
from categories.serializers import CategorySerializer


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = (
            "name",
            "description",
        )


class RoomDetailSerializer(serializers.ModelSerializer):

    owner = TinyUserSErializer(read_only=True) # 유저가 수정할수 없게 함
    amenities = AmenitySerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"
    
    def get_rating(self, room):
        return room.rating()


class RoomListSerializer(serializers.ModelSerializer):

    rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Room
        fields = (
            "pk",
            "name",
            "country",
            "city",
            "price",
            "rating",
        )

    def get_rating(self, room):
        return room.rating()
