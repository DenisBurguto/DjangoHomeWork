from decimal import Decimal

from django.contrib import admin
from .models import Client, Product, Order

DISCOUNT = 10


@admin.action(description="apply  discount")
def apply_discount(modeladmin, request, queryset):
    for product in queryset:
        product.price -= (product.price * Decimal(DISCOUNT / 100))
        product.save()


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'photo']
    ordering = ['-quantity']
    list_filter = ['created_at', 'price', 'quantity']
    search_fields = ['description', 'name']
    search_help_text = 'seach in names and descriptions'
    actions = [apply_discount]
    readonly_fields = ['created_at']
    fieldsets = [
        ('main', {'classes': ['wide'], 'fields': ['name', 'price', 'quantity']}),
        ('description', {'classes': ['collapse'], 'fields': ['description', 'photo']}),
        ('created_at', {'fields': ['created_at']}),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_amount', 'date_ordered']
    ordering = ['-date_ordered', '-total_amount', ]
    search_fields = ['customer', 'total_amount']
    search_help_text = 'seach a customer or total amount'
    readonly_fields = ['customer', 'total_amount', 'products']
    list_filter = ['customer', 'total_amount']
    fieldsets = [
        ('main', {'classes': ['wide'], 'fields': ['customer', 'total_amount', 'date_ordered']}),
        ('products', {'classes': ['collapse'], 'fields': ['products']})
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client)

# Register your models here.
