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
    owner = ForeignKey('auth.User', related_name='listings', null=True, on_delete=CASCADE)

    # Fixed Data
    asking_price = IntegerField()
    volume = IntegerField()
    water_type = CharField(max_length=50,)
    partial_listing = BooleanField(default=False)
    minimum_increment = IntegerField(blank=True, null=True)

    # Changing Data
    twai_confirmed = BooleanField(default=False)
    active = BooleanField(default=True)

    def save_model(self, request, obj, form, change):
        if not change:
            obj.owner = request.user
        obj.save()

    def __str__(self):
        return f"{self.pk} | {self.volume} AF for ${self.asking_price}/AF"