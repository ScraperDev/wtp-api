from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('listings.urls')),
    path('token/', TokenObtainPairView.as_view(), name="token_obtain"),
    path('refresh/', TokenRefreshView.as_view(), name="token_refresh"),
]
