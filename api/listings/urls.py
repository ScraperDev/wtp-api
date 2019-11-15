from django.urls import path
from listings.views.listing_view_set import ListingViewSet
from rest_framework.urlpatterns import format_suffix_patterns

listing_list = ListingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

listing_detail = ListingViewSet.as_view({
    'get': 'retrieve',
    'patch': 'set_inactive',
})

urlpatterns = format_suffix_patterns([
    path('listings/', listing_list, name='listing-list'),
    path('listings/<int:pk>/', listing_detail, name='listing-detail'),
])
