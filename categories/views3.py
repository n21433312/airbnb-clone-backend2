from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class Categories(APIView):

    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(): #is_valid 유저가 보낸 데이터가 유효한지 검사하는기능
            new_category = serializer.save() #create 실행, 사용자 데이터만으로 serializer 만들기 때문
            return Response(CategorySerializer(new_category).data, ) 
        else:
            return Response(serializer.errors) 


class CategoryDetail(APIView):
    
    def get_object(self, pk): 
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound
        return category

    def get(self, request, pk): #url안의 pk를 요청하고있기 때문에
        serializer = CategorySerializer(self.get_object(pk))
        return Response(serializer.data)
    
    def put(self, request, pk): #url안의 pk를 요청하고있기 때문에
        serializer = CategorySerializer(
            self.get_object(pk), 
            data=request.data, 
            partial=True, #모든데이터 변경이아닌 일부만 변경 하고싶을때
        )
        if serializer.is_valid():
            updated_category = serializer.save() #create가 아닌 update실행, 사용자 데이터 + DB의 데이터로 serializer를 만들기 때문
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)    
        
    def delete(self, request, pk): #url안의 pk를 요청하고있기 때문에
        self.get_object(pk).delete()
        return Response(status=HTTP_204_NO_CONTENT)