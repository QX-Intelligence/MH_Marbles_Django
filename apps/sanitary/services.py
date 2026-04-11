from .models import SanitaryProduct


class SanitaryService:

    @staticmethod
    def get_all_products():
        return SanitaryProduct.objects.all()

    @staticmethod
    def create_product(data):
        return SanitaryProduct.objects.create(**data)

    @staticmethod
    def delete_product(product):
        product.delete()