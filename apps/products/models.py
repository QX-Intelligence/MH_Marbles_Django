from django.db import models
from django.conf import settings

class Category(models.Model):

    name = models.CharField(max_length=100)

    slug = models.SlugField(unique=True)

    image_key = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if not self.image_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.image_key)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=200)

    company = models.ForeignKey(
        "companies.Company",
        on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    size = models.CharField(max_length=50)

    color = models.CharField(max_length=50)

    finish = models.CharField(max_length=50)

    sku = models.CharField(max_length=100, unique=True)

    image_key = models.CharField(max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if not self.image_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.image_key)

    def __str__(self):
        return self.name