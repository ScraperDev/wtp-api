from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_500_INTERNAL_SERVER_ERROR

from listings.serializers.listing_serializer import ListingSerializer
from listings.models.listing_model import Listing
from listings.permissions.owner_permission import IsOwnerOrReadOnly

# Create your views here.
class ListingViewSet(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    """
    Retrieves, Lists, Creates, or Partially Updates a model.
    """
    queryset = Listing.objects.filter(active=True)
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    # Overrides the perform_create method in the Create Mixin
    def perform_create(self, serializer):
        """
        Overrides the perform_create method in the create mixin.
        This is done to add the "owner" field.
        """
        serializer.save(owner=self.request.user)

    def set_inactive(self, request, *args, **kwargs):
        """
        Sets the active property to false. Effectively a "DELETE"
        on the object from end-user standpoint.
        Will 404 if run more than once, since the queryset only adjusts active listings.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={ 'active': False }, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response('', status=HTTP_204_NO_CONTENT)
        else:
            # This should never trigger
            return Response(serializer.errors, status=HTTP_500_INTERNAL_SERVER_ERROR) 
