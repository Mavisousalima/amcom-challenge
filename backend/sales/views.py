from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sale
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
            serializer.save()
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