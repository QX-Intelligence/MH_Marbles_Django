from django.db import models

class CarouselSlide(models.Model):
    image_key = models.CharField(max_length=500, blank=True, null=True)
    heading = models.CharField(max_length=200, blank=True)
    subtext = models.CharField(max_length=300, blank=True)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_link = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_image_url(self):
        if not self.image_key:
            return None
        from core.s3 import generate_presigned_url
        return generate_presigned_url(self.image_key)

    def __str__(self):
        return self.heading or f"Slide {self.order}"
    
    class Meta:
        ordering = ['order', '-created_at']
