from django.db import models

class SanitaryProduct(models.Model):

    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        "products.Category",
        on_delete=models.CASCADE,
        related_name="sanitary_products",
        null=True,
        blank=True
    )

    description = models.TextField(blank=True)

    image_key = models.CharField(max_length=500, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if not self.image_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.image_key)

    def __str__(self):
        return self.name