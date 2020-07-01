from django.urls import path
from .views import PostViewset, UserViewset
from rest_framework.routers import SimpleRouter


routers = SimpleRouter()
routers.register('users', UserViewset, basename='users')
routers.register('', PostViewset, basename='posts')

urlpatterns = routers.urls















