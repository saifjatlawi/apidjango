from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Client
from .serializers import ClientSerializer

class ListClient(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)
class AddClientView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetClientView(APIView):
    def get(self, request,id):
        clients = Client.objects.get(client_id=id)
        serializer = ClientSerializer(clients)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

class UpdateClientView(APIView):
    def put(self, request, id, *args, **kwargs):
        try:
            client = Client.objects.get(client_id=id) 
            serializer = ClientSerializer(client, data=request.data)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"},status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id, *args, **kwargs):
        try:
            client = Client.objects.get(client_id=id)
            serializer = ClientSerializer(client, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"},status=status.HTTP_404_NOT_FOUND)
    
class DeleteClientView(APIView):
    def delete(self, request,id,*args, **kwargs):
        try:
            client = Client.objects.get(client_id=id)  
            client.delete()  
            return Response({"message": "Client deleted successfully"}, status=status.HTTP_200_OK)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        