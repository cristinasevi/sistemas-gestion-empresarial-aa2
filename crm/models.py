from django.db import models
from core.models import Cliente

class Oportunidad(models.Model):
    class Etapa(models.TextChoices):
        PROSPECCION = 'PRO', 'Prospección'
        PROPUESTA = 'PRP', 'Propuesta'
        NEGOCIACION = 'NEG', 'Negociación'
        GANADA = 'GAN', 'Cerrada Ganada'
        PERDIDA = 'PER', 'Cerrada Perdida'

    titulo = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='oportunidades')
    valor_estimado = models.DecimalField(max_digits=12, decimal_places=2)
    etapa = models.CharField(max_length=3, choices=Etapa.choices, default=Etapa.PROSPECCION)
    fecha_cierre = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} — {self.get_etapa_display()}"
