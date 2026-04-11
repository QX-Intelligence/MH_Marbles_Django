from rest_framework import serializers
from .models import Company
from core.s3 import upload_file


class CompanySerializer(serializers.ModelSerializer):
    logo_url = serializers.SerializerMethodField()
    logo = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = Company
        fields = "__all__"
        extra_kwargs = {
            'logo_key': {'required': False}
        }

    def get_logo_url(self, obj):
        return obj.get_logo_url()

    def create(self, validated_data):
        logo = validated_data.pop('logo', None)
        if logo:
            key = upload_file(logo, "companies")
            validated_data['logo_key'] = key
        return super().create(validated_data)

    def update(self, instance, validated_data):
        logo = validated_data.pop('logo', None)
        if logo:
            key = upload_file(logo, "companies")
            validated_data['logo_key'] = key
        return super().update(instance, validated_data)