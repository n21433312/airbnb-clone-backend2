from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields =  "__all__" #필드를 하나씩 보여주거나 몇몇개를 제외하거나 전부 보여줄수 있음.