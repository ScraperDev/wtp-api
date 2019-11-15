from listings.models.listing_model import Listing
from rest_framework.serializers import ModelSerializer, IntegerField, BooleanField, CharField

class ListingSerializer(ModelSerializer):
    asking_price = IntegerField()
    volume = IntegerField()
    partial_listing = BooleanField()
    minimum_increment = IntegerField()
    water_type = CharField()
    
    class Meta:
        model = Listing
        fields = ('created_date', 'owner', 'asking_price', 'volume', 'partial_listing', 'minimum_increment', 'water_type', 'twai_confirmed', 'active')