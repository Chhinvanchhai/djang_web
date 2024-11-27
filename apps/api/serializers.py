from rest_framework import serializers
# In api/views.py or api/serializers.py
from product.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include the fields you want from Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Use the CategorySerializer here

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'created_at', 'updated_at', 'image', 'category']
