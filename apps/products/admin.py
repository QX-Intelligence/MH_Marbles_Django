from django.contrib import admin
from .models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ("name", "company", "category", "size", "finish")

    search_fields = ("name", "sku")

    list_filter = ("company", "category", "finish")


admin.site.register(Category)