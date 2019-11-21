from django.db.models import Model, IntegerField, ForeignKey, CASCADE

class Offer(Model):
    """
    ### Offer Model
    #### Fields
    - created_date: 
    - offering_on: Listing that the offer is being made on
    - offer_price: Amount being offered, in $ per Acre Foot
    - requested_volume: How much of the water the offerer wants, in Acre Feet
    """

    offering_on = ForeignKey('listings.Listing', on_delete=CASCADE, related_name="offers")
    offer_price = IntegerField()
    requested_volume = IntegerField()
