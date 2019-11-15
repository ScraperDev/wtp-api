from django.urls import path
from listings.views.ListingViewSet import ListingViewSet

listing_list = ListingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

listing_detail = ListingViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
})

urlpatterns = format_suffix_patterns([
    path('listings/', listing_list, name='listing-list'),
    path('listings/<int:pk>/', listing_detail, name='listing-detail'),
])