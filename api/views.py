from rest_framework.viewsets import ModelViewSet

from .models import Box, Order, Pizza, Topping
from .serializers import (
    BoxSerializer,
    OrderDetailsSerializer,
    OrderSummarySerializer,
    PizzaSerializer,
    ToppingSerializer,
)


# Create your views here.
class ToppingViewSet(ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class PizzaViewSet(ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class BoxViewSet(ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()

    def get_serializer_class(self):
        if self.action in ("create", "update","partial_update"):
            return OrderSummarySerializer
        return OrderDetailsSerializer