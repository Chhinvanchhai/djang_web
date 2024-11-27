from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'category', CategoryViewSet, basename='category')
# app_name = 'api' 
print("-----------------------------------")
print(router.urls)
urlpatterns = router.urls
