from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Seller
from .serializers import SellerSerializer


class SellerListView(APIView):
    def get(self, request):
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)
    
class SellerDetailView(APIView):
    def get(self, request, pk):
          try:
              seller = Seller.objects.get(pk=pk)
          except Seller.DoesNotExist:
               return Response({"message": "Seller not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = SellerSerializer(seller)
          return Response(serializer.data)


class SellerUpdateView(APIView):
     def put(self, request, pk):
          try:
            seller = Seller.objects.get(pk=pk)
          except Seller.DoesNotExist:
               return Response({"message": "Seller not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = SellerSerializer(seller, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class SellerDeleteView(APIView):
     def delete(self, request, pk):
          try:
               seller = Seller.objects.get(pk=pk)
          except Seller.DoesNotExist:
               return Response({"message": "Seller not found"}, status=status.HTTP_404_NOT_FOUND)
          
          seller.delete()
          return Response({"message": "Seller deleted"}, status=status.HTTP_204_NO_CONTENT)