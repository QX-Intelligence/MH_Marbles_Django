from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    logo_key = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_logo_url(self):
        if not self.logo_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.logo_key)

    def __str__(self):
        return self.name