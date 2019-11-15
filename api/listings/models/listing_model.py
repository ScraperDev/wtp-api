from django.db.models import Model, IntegerField, BooleanField, CharField, DateTimeField, ForeignKey, CASCADE
from django.utils import timezone
from django.conf import settings

class Listing(Model):
    """
    Broken into three field types:
    ### Metadata
    - created_date
    - owner

    ### Fixed Data
    - asking_price
    - volume
    - partial_listing
    - minimum_increment
    - water_type
    
    ### Editable Data
    - twai_confirmed
    - active

    """
    # Metadata
    created_date = DateTimeField(auto_now_add=True)
    owner = ForeignKey('auth.User', related_name='listings', on_delete=CASCADE)

    # Fixed Data
    asking_price = IntegerField(editable=False)
    volume = IntegerField(editable=False)
    water_type = CharField(max_length=50, editable=False)
    partial_listing = BooleanField(default=False, editable=False)
    minimum_increment = IntegerField(blank=True, null=True, editable=False)

    # Changing Data
    twai_confirmed = BooleanField(default=False)
    active = BooleanField(default=True)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.usera

    def __str__(self):
        return f"{self.created_date} listing for {self.volume} AF"