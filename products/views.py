from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductDetailView(APIView):
    def get(self, request, code):
          try:
              product = Product.objects.get(code=code)
          except Product.DoesNotExist:
               return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = ProductSerializer(product)
          return Response(serializer.data)


class ProductUpdateView(APIView):
     def put(self, request, code):
          try:
            product = Product.objects.get(code=code)
          except Product.DoesNotExist:
               return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = ProductSerializer(product, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class ProductDeleteView(APIView):
     def delete(self, request, code):
          try:
               product = Product.objects.get(code=code)
          except Product.DoesNotExist:
               return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
          
          product.delete()
          return Response({"message": "Product deleted"}, status=status.HTTP_204_NO_CONTENT)