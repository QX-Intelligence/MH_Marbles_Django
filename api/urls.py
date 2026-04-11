from django.urls import path, include
from .router import urlpatterns as router_urls
from core.thumbnail import thumbnail_view

urlpatterns = [
    path("", include(router_urls)),
    path("thumbnail/", thumbnail_view, name="thumbnail"),
]