import uuid

from django.db import models

# Create your models here.

class Order(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    customer = models.CharField(max_length=256, blank=False, null=False)

    address = models.CharField(max_length=512, blank=False, null=False)

class Box(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    color = models.CharField(primary_key=True,
                             max_length=64
    )


class Topping(models.Model):
    name = models.CharField(max_length=64,
                            primary_key=True)

class Pizza(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    order = models.ForeignKey(Order,
                               on_delete=models.CASCADE,
                               related_name="pizzas",
                               null=False)
    box = models.OneToOneField(
        Box,
        on_delete=models.SET_NULL,
        related_name="contents",
        null=True
    )

    toppings = models.ManyToManyField(Topping,
                                      related_name="+")
