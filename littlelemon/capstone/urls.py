from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Restaurant HTML views
    path('restaurant/', include('restaurant.urls')),
    # API endpoints
    path('api/', include('api.urls')),
    # Djoser auth (user registration & token login)
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
