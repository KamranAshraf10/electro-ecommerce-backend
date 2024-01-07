from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer


# ViewSet
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
