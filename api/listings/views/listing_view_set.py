from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from listings.serializers import ListingSerializer
from listings.models.isting import Listing
from listings.permissions import IsOwnerOrReadOnly

# Create your views here.
class ListingViewSet(ModelViewSet):
    """
    Read-Only Viewset for getting all or one Listing.
    Authed users only.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    