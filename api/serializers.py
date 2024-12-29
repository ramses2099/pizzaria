from rest_framework import serializers

from .function import attempt_json_deserialize
from .models import Box, Order, Pizza, Topping


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ["id","color"]

class OrderSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id","customer","address"]

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ["name"]

class PizzaSerializer(serializers.ModelSerializer):
    # Nested serializers
    order = OrderSummarySerializer(read_only=True)
    box = BoxSerializer(read_only=True)
    toppings = ToppingSerializer(many=True, read_only=True)
    
    class Meta:
        model = Pizza
        fields = ["id","order", "box", "toppings"]
    
    def create(self, validated_data):
        request = self.context["request"]

        order_pk = request.data.get("order")
        order_pk = attempt_json_deserialize(order_pk, expect_type=str)
        validated_data["order_id"] = order_pk

        box_data = request.data.get("box")
        box_data = attempt_json_deserialize(box_data, expect_type=dict)
        box = Box.objects.create(**box_data)
        validated_data["box"] = box

        toppings_data = request.data.get("toppings")
        toppings_data = attempt_json_deserialize(toppings_data, expect_type=list)
        toppings_objs = [Topping.objects.create(**data) for data in toppings_data]
        validated_data["toppings"] = toppings_objs

        instance = super().create(validated_data)

        return instance
    
    def update(self, instance, validated_data):
        request = self.context["request"]

        order_data = request.data.get("order")
        order_data = attempt_json_deserialize(order_data, expect_type=str)
        validated_data["order"] = order_data

        box_data = request.data.get("box")
        box_data = attempt_json_deserialize(box_data, expect_type=dict)
        box = Box.objects.create(**box_data)
        validated_data["box"] = box

        topppings_data =  request.data.get("toppings")
        toppings_ids = attempt_json_deserialize(topppings_data, expect_type=list)
        validated_data["toppings"] = toppings_ids

        instance = super().update(instance, validated_data)

        return instance

class PizzaSummaryserializer(serializers.ModelSerializer):
    box = BoxSerializer(read_only=True)

    class Meta:
        model = Pizza
        fields = ["id","box","toppings"]

class OrderDetailsSerializer(serializers.ModelSerializer):
    pizzas = PizzaSummaryserializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ["id","customer","address","pizzas"]