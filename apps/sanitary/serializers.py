from rest_framework import serializers
from .models import SanitaryProduct
from apps.products.models import Category
from core.s3 import upload_file


class SanitaryCategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Category
        fields = "__all__"
        extra_kwargs = {
            'image_key': {'required': False}
        }

    def get_image_url(self, obj):
        return obj.get_image_url()

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "sanitary/categories")
            validated_data['image_key'] = key
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "sanitary/categories")
            validated_data['image_key'] = key
        return super().update(instance, validated_data)


class SanitarySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = SanitaryProduct
        fields = "__all__"
        extra_kwargs = {
            'image_key': {'required': False}
        }

    def get_image_url(self, obj):
        return obj.get_image_url()

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "sanitary/products")
            validated_data['image_key'] = key
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "sanitary/products")
            validated_data['image_key'] = key
        return super().update(instance, validated_data)