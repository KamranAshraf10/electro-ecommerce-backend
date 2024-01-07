from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet


router = DefaultRouter()
router.register(r"users", ProductViewSet)


urlpatterns = [
    # DRF viewset
    path("api/products", include(router.urls)),
]
