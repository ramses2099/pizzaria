from django.contrib import admin

# Register your models here.
from .models import Box, Order, Pizza, Topping


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'address']

admin.site.register(Order, OrderAdmin)

class PizzaAdmin(admin.ModelAdmin):
    list_display = ['id']

admin.site.register(Pizza, PizzaAdmin)

class ToppingAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Topping, ToppingAdmin)

class BoxAdmin(admin.ModelAdmin):
    list_display = ['color']

admin.site.register(Box, BoxAdmin)