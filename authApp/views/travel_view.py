from rest_framework import views, status
from rest_framework.response import Response
from rest_framework import generics

from authApp.models import Travel
from authApp.serializers import TravelSerializer
# Traditional way


class TravelView(views.APIView):
    def get(self, request):
        queryset = Travel.objects.all()
        serialized = TravelSerializer(queryset, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

#Generics methods
# List all users and create a new one
class TravelListCreateView(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

# Retrieve, Update and Delete users
class TravelRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer

# Search by fk
class TravelFkView(generics.ListAPIView):
    serializer_class = TravelSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        id = self.kwargs['id_manager']
        return Travel.objects.filter(id_manager=id)
