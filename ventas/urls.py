from django.urls import path
from .api_views import ProductoListAPIView

urlpatterns = [
    path('productos/', ProductoListAPIView.as_view(), name='api_productos'),
]
