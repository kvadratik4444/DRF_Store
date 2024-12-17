from rest_framework import serializers

from goods.models import Products


class ProductSerializer(serializers.ModelSerializer):
    sell_price = serializers.ReadOnlyField()

    class Meta:
        model = Products
        fields = '__all__'