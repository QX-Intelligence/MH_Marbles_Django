from .models import ProductCollection

class CollectionService:

    @staticmethod
    def get_all_collections():
        return ProductCollection.objects.all()

    @staticmethod
    def get_collection(collection_id):
        return ProductCollection.objects.get(id=collection_id)

    @staticmethod
    def create_collection(data):
        return ProductCollection.objects.create(**data)

    @staticmethod
    def update_collection(collection, data):
        for key, value in data.items():
            setattr(collection, key, value)
        collection.save()
        return collection

    @staticmethod
    def delete_collection(collection):
        collection.delete()
