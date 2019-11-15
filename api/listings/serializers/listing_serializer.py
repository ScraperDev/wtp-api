from listings.models.listing_model import Listing
from rest_framework.serializers import ModelSerializer

class ListingSerializer(ModelSerializer):
    class Meta:
        model = Listing
        fields = ['created_date', 'owner', 'asking_price', 'volume', 'partial_listing', 'minimum_increment', 'water_type', 'twai_confirmed', 'active']