from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

class ProductDetail(APIView):
        def get(self, request, *args, **kwargs):
             code = self.kwargs.get('code')
             product = Product.objects.get(code=code)
             serializer = ProductSerializer(product)
             return Response(serializer.data)