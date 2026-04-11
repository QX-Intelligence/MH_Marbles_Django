from django.contrib import admin
from .models import ProductCollection


@admin.register(ProductCollection)
class ProductCollectionAdmin(admin.ModelAdmin):

    list_display = ("name", "created_at")

    filter_horizontal = ("products",)