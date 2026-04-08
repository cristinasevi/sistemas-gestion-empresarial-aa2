import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pedido

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Pedido)
def descontar_stock(sender, instance, **kwargs):
    if instance.estado.codigo == 'CONFIRMADO':
        for linea in instance.lineas.all():
            producto = linea.producto
            if producto.stock >= linea.cantidad:
                producto.stock -= int(linea.cantidad)
                producto.save()
            else:
                logger.error(
                    f"Stock insuficiente para {producto.nombre}. "
                    f"Stock: {producto.stock}, solicitado: {linea.cantidad}"
                )
