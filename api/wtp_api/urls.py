from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/listings/', include('listings.urls')),
    path('api/token/', TokenObtainSlidingView.as_view(), name="token_obtain"),
    path('api/refresh/', TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
