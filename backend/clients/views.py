from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Client
from .serializers import ClientSerializer


class ClientListView(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
    
class ClientDetailView(APIView):
    def get(self, request, pk):
          try:
              client = Client.objects.get(pk=pk)
          except Client.DoesNotExist:
               return Response({"message": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = ClientSerializer(client)
          return Response(serializer.data)


class ClientCreateView(APIView):
     def post(self, request):
          serializer = ClientSerializer(data=request.data)

          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_201_CREATED)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientUpdateView(APIView):
     def put(self, request, pk):
          try:
            client = Client.objects.get(pk=pk)
          except Client.DoesNotExist:
               return Response({"message": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
          
          serializer = ClientSerializer(client, data=request.data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     

class ClientDeleteView(APIView):
     def delete(self, request, pk):
          try:
               client = Client.objects.get(pk=pk)
          except Client.DoesNotExist:
               return Response({"message": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
          
          client.delete()
          return Response({"message": "Client deleted"}, status=status.HTTP_204_NO_CONTENT)