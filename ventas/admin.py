from django.contrib import admin
from .models import Pedido, LineaPedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'fecha_pedido', 'total', 'cliente', 'estado')
    search_fields = ('cliente__nombre', 'cliente__email', 'id')

@admin.register(LineaPedido)
class LineaPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pedido', 'producto', 'cantidad', 'precio_unitario')
