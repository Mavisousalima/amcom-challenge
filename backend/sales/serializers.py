from rest_framework import serializers

from .models import Sale
from products.serializers import ProductSerializer


class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    class Meta:
        model = Sale
        fields = '__all__'