from rest_framework import viewsets
from .models import CarouselSlide
from .serializers import CarouselSlideSerializer

class CarouselSlideViewSet(viewsets.ModelViewSet):
    queryset = CarouselSlide.objects.all()
    serializer_class = CarouselSlideSerializer
