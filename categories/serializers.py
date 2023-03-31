from rest_framework.serializers import ModelSerializer
from .models import Category

class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields =  "__all__" #필드를 하나씩[fields="name","kind",)] 보여주거나 몇몇개를 제외[exclude("created_at",)]하거나 전부[fields =  "__all__"] 보여줄수 있음.