from django.contrib.admin import register, site, ModelAdmin, TabularInline
from listings.models.listing_model import Listing
from listings.models.offer_model import Offer

site.register(Offer)

class InlineOfferAdmin(TabularInline):
    model = Offer

@register(Listing)
class ListingAdmin(ModelAdmin):
    inlines = [
        InlineOfferAdmin
    ]