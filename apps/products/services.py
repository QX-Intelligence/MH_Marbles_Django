from .models import Product


class ProductService:

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_product(product_id):
        return Product.objects.get(id=product_id)

    @staticmethod
    def create_product(data):
        return Product.objects.create(**data)

    @staticmethod
    def update_product(product, data):

        for key, value in data.items():
            setattr(product, key, value)

        product.save()

        return product

    @staticmethod
    def delete_product(product):
        product.delete()