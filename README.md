# MiniERP - Sistemas de Gestión Empresarial AA2

## Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Instalación y Uso](#instalación-y-uso)
- [Fase 1: Lógica de Negocio y UI](#fase-1-lógica-de-negocio-y-ui)
  - [1.1 Formularios y Validación](#11-formularios-y-validación)
  - [1.2 Cálculos Automáticos](#12-cálculos-automáticos)
- [Fase 2: Automatización y Módulo CRM](#fase-2-automatización-y-módulo-crm)
  - [2.1 Señales (Signals)](#21-señales-signals)
  - [2.2 Pipeline de CRM](#22-pipeline-de-crm)

## Descripción

Evolución del MiniERP con lógica de negocio, automatización mediante signals, gestión del embudo de ventas (CRM) y despliegue profesional.

## Tecnologías

- Python 3.13
- Django 6.0.1
- SQLite3

## Instalación y Uso
```bash
# Activar entorno virtual
.\venv\Scripts\activate

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```
Acceder al panel de administración en: http://127.0.0.1:8000/admin

---

## Fase 1: Lógica de Negocio y UI

### 1.1 Formularios y Validación

Se han creado dos formularios en `ventas/forms.py`:

- **ProductoForm**: Valida que el stock nunca sea inferior a 0.
- **ClienteForm**: Valida que el email tenga dominio corporativo (`@empresa.com`). La unicidad del DNI/CIF ya está garantizada por el modelo (`unique=True`).

### 1.2 Cálculos Automáticos

Se ha implementado `calcular_totales()` en el modelo `Pedido` usando el tipo `Decimal`:

- **Base** = suma de (precio_unitario × cantidad) de todas las líneas
- **IVA** = Base × 0.21
- **Total** = Base + IVA

El método se ejecuta automáticamente cada vez que se guarda una `LineaPedido` mediante `save()`.

---

## Fase 2: Automatización y Módulo CRM

### 2.1 Señales (Signals)

Se ha implementado una `post_save` signal en `ventas/signals.py` sobre el modelo `Pedido`:

- Cuando el estado cambia a `CONFIRMADO`, descuenta automáticamente el stock de cada producto incluido en las líneas del pedido.
- Si no hay stock suficiente, se registra un error en los logs sin modificar el stock.

### 2.2 Pipeline de CRM

Se ha creado la app `crm` con el modelo `Oportunidad`, que incluye los campos: título, cliente, valor estimado, etapa y fecha de cierre.

Las etapas del pipeline son: Prospección, Propuesta, Negociación, Cerrada Ganada, Cerrada Perdida.

#### KPI: Tasa de Conversión

La tasa de conversión mide el porcentaje de oportunidades que acaban en venta cerrada.

**Fórmula:**
Tasa de Conversión = (Oportunidades "Cerrada Ganada" / Total de oportunidades) × 100

**Cómo se calcularía con los datos del modelo:**
```python
total = Oportunidad.objects.count()
ganadas = Oportunidad.objects.filter(etapa='GAN').count()
tasa = (ganadas / total) * 100 if total > 0 else 0
```
