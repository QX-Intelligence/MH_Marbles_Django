from rest_framework import serializers
from .models import ProductCollection
from core.s3 import upload_file

class ProductCollectionSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    cover_image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = ProductCollection
        fields = "__all__"
        extra_kwargs = {
            'image_key': {'required': False}
        }

    def get_image_url(self, obj):
        return obj.get_image_url()

    def create(self, validated_data):
        cover_image = validated_data.pop('cover_image', None)
        if cover_image:
            key = upload_file(cover_image, "collections")
            validated_data['image_key'] = key
        return super().create(validated_data)

    def update(self, instance, validated_data):
        cover_image = validated_data.pop('cover_image', None)
        if cover_image:
            key = upload_file(cover_image, "collections")
            validated_data['image_key'] = key
        return super().update(instance, validated_data)