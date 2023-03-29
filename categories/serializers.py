from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.Serializer):

    
    pk = serializers.IntegerField(read_only=True) # read_only=True 유저에게 값을 받지않을때 사용
    name = serializers.CharField(required=True, max_length=50, )
    kind = serializers.ChoiceField(choices=Category.CategoryKindChoices.choices, )
    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
       return Category.objects.create(**validated_data)