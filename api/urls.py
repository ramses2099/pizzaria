from django.urls import include, path
from rest_framework import routers

from .views import (
    BoxViewSet,
    OrderViewSet,
    PizzaViewSet,
    ToppingViewSet,
)

router = routers.DefaultRouter()

router.register(r"orders", OrderViewSet, "orders")

router.register(r"pizzas", PizzaViewSet, "pizzas")

router.register(r"boxes", BoxViewSet, "boxes")

router.register(r"toppings", ToppingViewSet, "toppings")


urlpatterns = [
    path("pizzaria/", include(router.urls)),
]
