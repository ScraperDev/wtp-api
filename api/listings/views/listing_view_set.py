from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

from listings.serializers.listing_serializer import ListingSerializer
from listings.models.listing_model import Listing
from listings.permissions.owner_permission import IsOwnerOrReadOnly

# Create your views here.
class ListingViewSet(RetrieveModelMixin, ListModelMixin, CreateModelMixin, GenericViewSet):
    """
    Read-Only Viewset for getting all or one Listing.
    Authed users only.
    """
    queryset = Listing.objects.filter(active=True)
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)