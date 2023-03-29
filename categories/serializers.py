from rest_framework import serializers

class CategorySerializer(serializers.Serializer):

    
    pk = serializers.IntegerField(read_only=True) # read_only=True 유저에게 값을 받지않을때 사용
    name = serializers.CharField(required=True, max_length=50, )
    kind = serializers.CharField(max_length=15, )
    created_at = serializers.DateTimeField(read_only=True)