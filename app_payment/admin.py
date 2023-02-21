from django.contrib import admin
from .models import Item, Order, Discount, Tax


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = 'id', 'name', 'description', 'price'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = 'user', 'id'


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
	pass


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
	pass
