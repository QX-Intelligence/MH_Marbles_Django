from django.db import models


class ProductCollection(models.Model):

    name = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    image_key = models.CharField(max_length=500, blank=True, null=True)

    products = models.ManyToManyField(
        "products.Product",
        related_name="collections",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if not self.image_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.image_key)

    def __str__(self):
        return self.name