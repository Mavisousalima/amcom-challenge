from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sale, SaleItem
from products.models import Product
from .serializers import SaleSerializer


class SaleListView(APIView):
    def get(self, request):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)
    
    
class SaleDetailView(APIView):
    def get(self, request, pk):
        try:
            seller = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"message": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
          
        serializer = SaleSerializer(seller)
        return Response(serializer.data)


class SaleCreateView(APIView):
    def post(self, request):
        serializer = SaleSerializer(data=request.data)

        if serializer.is_valid():
            sale = serializer.save()

            # Process the products and create SaleItem objects
            products_data = request.data.get('products', [])
            for product_data in products_data:
                product_id = product_data.get('id')
                quantity_sold = product_data.get('quantity', 1)  # Default to 1 if quantity is not provided

                # Fetch the product
                try:
                    product = Product.objects.get(pk=product_id)
                except Product.DoesNotExist:
                    return Response({"message": f"Product with ID {product_id} not found"}, status=status.HTTP_404_NOT_FOUND)

                # Create the SaleItem
                SaleItem.objects.create(sale=sale, product=product, quantity_sold=quantity_sold)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleUpdateView(APIView):
    def put(self, request, pk):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"message": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
          
        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SaleDeleteView(APIView):
     def delete(self, request, pk):
        try:
            sale = Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            return Response({"message": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)
        
        sale.delete()
        return Response({"message": "Sale deleted"}, status=status.HTTP_204_NO_CONTENT)