from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    dni = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Producto(models.Model):
    sku = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_iva = models.DecimalField(max_digits=4, decimal_places=2, default=21.00)
    
    def __str__(self):
        return f"{self.sku} - {self.nombre}"

class EstadoPedido(models.Model):
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('CONFIRMADO', 'Confirmado'),
        ('FACTURADO', 'Facturado'),
        ('COBRADO', 'Cobrado'),
    ]
    
    codigo = models.CharField(max_length=20, unique=True, choices=ESTADOS)
    
    def __str__(self):
        return self.codigo
