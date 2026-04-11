from rest_framework import serializers
from .models import Product, Category
from core.s3 import upload_file


class CategorySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_image_url(self, obj):
        return obj.get_image_url()


class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Product
        fields = "__all__"
        extra_kwargs = {
            'image_key': {'required': False}
        }

    def get_image_url(self, obj):
        return obj.get_image_url()

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "products")
            validated_data['image_key'] = key
        elif 'image_key' not in validated_data:
            raise serializers.ValidationError({"image_key": "This field is required."})
        return super().create(validated_data)

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            key = upload_file(image, "products")
            validated_data['image_key'] = key
        return super().update(instance, validated_data)