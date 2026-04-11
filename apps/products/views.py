from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from core.s3 import upload_file

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter

from core.pagination import ProductCursorPagination


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = None # No pagination for categories usually


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all().order_by("-created_at")

    serializer_class = ProductSerializer

    pagination_class = ProductCursorPagination

    filter_backends = [DjangoFilterBackend]

    filterset_class = ProductFilter

    filterset_fields = [
        "company",
        "category",
        "size",
        "color",
        "finish",
    ]

    @action(detail=False, methods=["POST"], url_path='upload')
    def upload_image(self, request):
        """
        Upload image to S3 and return object key.
        """
        file = request.FILES.get("image")

        if not file:
            return Response({"error": "Image file required"}, status=400)

        key = upload_file(file, "products")

        return Response({
            "key": key
        })