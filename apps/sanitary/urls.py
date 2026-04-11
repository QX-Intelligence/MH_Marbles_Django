from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("categories", views.SanitaryCategoryViewSet, basename="sanitary-category")
router.register("", views.SanitaryProductViewSet, basename="sanitary-product")

urlpatterns = [
    path("", include(router.urls)),
]