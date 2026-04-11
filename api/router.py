from rest_framework.routers import DefaultRouter

from apps.products.views import ProductViewSet, CategoryViewSet
from apps.companies.views import CompanyViewSet
from apps.product_collections.views import ProductCollectionViewSet
from apps.sanitary.views import SanitaryProductViewSet, SanitaryCategoryViewSet
from apps.contacts.views import ContactInquiryViewSet
from apps.hero_carousel.views import CarouselSlideViewSet


router = DefaultRouter()

router.register(r'products', ProductViewSet, basename="products")
router.register(r'categories', CategoryViewSet, basename="categories")
router.register(r'companies', CompanyViewSet, basename="companies")
router.register(r'collections', ProductCollectionViewSet, basename="collections")
router.register(r'sanitary/categories', SanitaryCategoryViewSet, basename="sanitary-categories")
router.register(r'sanitary', SanitaryProductViewSet, basename="sanitary")
router.register(r'contacts', ContactInquiryViewSet, basename="contacts")
router.register(r'hero_carousel', CarouselSlideViewSet, basename="hero_carousel")


urlpatterns = router.urls   