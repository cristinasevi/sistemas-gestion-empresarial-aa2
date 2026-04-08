from django.contrib import admin
from .models import Oportunidad

@admin.register(Oportunidad)
class OportunidadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'cliente', 'etapa', 'valor_estimado', 'fecha_cierre')
    list_filter = ('etapa',)
    search_fields = ('titulo', 'cliente__nombre')
