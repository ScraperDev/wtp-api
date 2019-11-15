from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import ListingSerializer
from .models.listing import Listing

# Create your views here.
class ListingViewSet(ModelViewSet):
    """
    Read-Only Viewset for getting all or one Listing.
    Authed users only.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    