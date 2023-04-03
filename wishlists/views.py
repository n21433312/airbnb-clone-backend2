from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from .serializers import WishlistSerializer

class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlist = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(all_wishlist, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
           whishlist =  serializer.save(user=request.user, )
           serializer = WishlistSerializer(whishlist)
           return Response(serializer.data)
        else:
            return Response(serializer.errors)
