from .models import Order
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer


# ViewSet
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]
