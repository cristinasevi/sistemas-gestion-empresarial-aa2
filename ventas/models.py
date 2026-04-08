from django.db import models
from decimal import Decimal
from core.models import Cliente, Producto, EstadoPedido

class Pedido(models.Model):
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_iva = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT, related_name='pedidos')
    estado = models.ForeignKey(EstadoPedido, on_delete=models.RESTRICT)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre} - Total: {self.total}"

    def calcular_totales(self):
        base = sum(
            linea.precio_unitario * linea.cantidad
            for linea in self.lineas.all()
        )
        self.total_base = Decimal(str(base))
        self.total_iva = self.total_base * Decimal('0.21')
        self.total = self.total_base + self.total_iva
        self.save()


class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='lineas')
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Línea {self.id}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.pedido.calcular_totales()

    class Meta:
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cantidad__gt=0),
                name='cantidad_positiva'
            ),
        ]
