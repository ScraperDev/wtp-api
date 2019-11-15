from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainSlidingView, TokenRefreshSlidingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listings.urls')),
    path('token/', TokenObtainSlidingView.as_view(), name="token_obtain"),
    path('refresh/', TokenRefreshSlidingView.as_view(), name="token_refresh"),
]
