from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from listings.serializers.listing_serializer import ListingSerializer
from listings.models.listing_model import Listing
from listings.permissions.owner_permission import IsOwnerOrReadOnly

# Create your views here.
class ListingViewSet(ModelViewSet):
    """
    Read-Only Viewset for getting all or one Listing.
    Authed users only.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    