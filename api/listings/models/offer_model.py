from django.db.models import Model, IntegerField, ForeignKey, CASCADE, DateTimeField

class Offer(Model):
    """
    ### Offer Model
    #### Fields
    - created_date: DateTime when the offer was made.
    - offering_on: Listing that the offer is being made on
    - offer_price: Amount being offered, in $ per Acre Foot
    - requested_volume: How much of the water the offerer wants, in Acre Feet
    """
    created_date = DateTimeField(auto_now_add=True)
    listing = ForeignKey('listings.Listing', on_delete=CASCADE, related_name='offers')
    owner = ForeignKey('auth.User', related_name='offers', null=True, on_delete=CASCADE)
    offer_price = IntegerField()
    requested_volume = IntegerField()

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def __str__(self):
        return f"{self.owner.username}'s offer on {self.listing.volume} AF."