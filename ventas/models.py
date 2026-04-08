from django.db import models
from core.models import Cliente, Producto, EstadoPedido

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, related_name='pedidos')
    estado = models.ForeignKey(EstadoPedido, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre} - Total: {self.total}"

    
class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Línea {self.id}"
    
    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cantidad__gt=0),
                name='cantidad_positiva'
            ),
        ]
