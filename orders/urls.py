from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.views import OrderViewSet

router = DefaultRouter()
router.register(r"users", OrderViewSet)

urlpatterns = [
    # DRF viewset
    path("api/orders", include(router.urls)),
]
