from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
import views
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'posts', views.PostViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.api_root),
    path('', include(router.urls)),
]

