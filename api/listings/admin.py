from django.contrib.admin import register, site, ModelAdmin, TabularInline
from listings.models.listing_model import Listing
from listings.models.offer_model import Offer

class InlineOfferAdmin(TabularInline):
    model = Offer

@register(Listing)
class ListingAdmin(ModelAdmin):
    readonly_fields = ('owner', 'asking_price', 'volume', 'water_type', 'partial_listing', 'minimum_increment')
    inlines = [
        InlineOfferAdmin
    ]

@register(Offer)
class OfferAdmin(ModelAdmin):
    readonly_fields = ('listing', 'offer_price', 'requested_volume', 'owner')