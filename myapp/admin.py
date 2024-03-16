from django.contrib import admin
from .models import Order, Product, Client


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')
    search_fields = ('id',)
    search_help_text = 'Search by id'
    list_filter = ('client',)
    list_per_page = 10
    date_hierarchy = 'order_date'
    ordering = ('-order_date',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'added_date')
    list_filter = ('added_date',)
    search_fields = ('description', 'name')
    search_help_text = 'Search by name or description'
    list_per_page = 100
    date_hierarchy = 'added_date'
    filter_horizontal = ()
    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
    )


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    list_filter = ('registration_date',)
    search_fields = ('phone_number', 'name')
    search_help_text = "Enter the phone number of the client or the name of the client"
    list_per_page = 10
    date_hierarchy = 'registration_date'
    filter_horizontal = ()
    fieldsets = (
        (None, {
            'fields': ('name', 'email', 'phone_number')
        }),
    )


admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
