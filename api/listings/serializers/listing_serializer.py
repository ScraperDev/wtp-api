from listings.models.listing_model import Listing
from rest_framework.serializers import ModelSerializer, IntegerField

class ListingSerializer(ModelSerializer):
    asking_price = IntegerField()
    class Meta:
        model = Listing
        fields = ('created_date', 'owner', 'asking_price', 'volume', 'partial_listing', 'minimum_increment', 'water_type', 'twai_confirmed', 'active')