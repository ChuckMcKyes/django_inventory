from rest_framework import serializers
from .models import InventoryItem, Categories


class InventoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ('id', 'name', 'manufacturer', 'model', 'serial_number',
                  'purchase_date', 'notes', 'category', 'image')

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class InventoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'