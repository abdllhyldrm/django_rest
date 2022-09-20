from cgitb import lookup
from favourite.api.paginations import FavouritePagination
from favourite.api.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from favourite.api.serializers import FavouriteListCreateAPISerializer, FavouriteAPISerializer 
from favourite.models import Favourite
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class FavouriteListCreateAPIView(ListCreateAPIView):
  queryset = Favourite.objects.all()
  serializer_class = FavouriteListCreateAPISerializer
  pagination_class = FavouritePagination
  permission_classes = [IsAuthenticated]
  
  def get_queryset(self):
    return Favourite.objects.filter(user=self.request.user)
  
  def perform_create(self, serializer):
    serializer.save(user = self.request.user)
    
class FavouriteAPIView(ListCreateAPIView):
  queryset = Favourite.objects.all()
  serializer_class = FavouriteAPISerializer  
  
class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
  queryset = Favourite.objects.all()
  serializer_class = FavouriteListCreateAPISerializer  
  lookup_field = 'pk' 
  permission_classes = [IsOwner]  