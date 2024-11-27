from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from product.models import Product, Category
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer, CategorySerializer

class ProductPagination(PageNumberPagination):
    page_size = 5  # You can set a custom page size here
    page_size_query_param = 'page_size'  # Allow clients to specify the page size
    max_page_size = 100  # Maximum number of items a client can request per page

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination  # 
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
