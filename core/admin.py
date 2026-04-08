from django.contrib import admin
from .models import Cliente, Producto, EstadoPedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'dni')
    search_fields = ('nombre', 'email', 'dni')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio_base', 'tipo_iva')
    search_fields = ('sku', 'nombre')

@admin.register(EstadoPedido)
class EstadoPedidoAdmin(admin.ModelAdmin):
    list_display = ('codigo',)
