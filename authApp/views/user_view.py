from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import generics

from authApp.models import User
from authApp.serializers import UserSerializer

# Traditional way
class UserView(views.APIView):
    def get (self, request):
        queryset = User.objects.all()
        serialized = UserSerializer(queryset, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

#Generics methods
# List all users and create a new one
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# Retrieve, Update and Delete users
class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer