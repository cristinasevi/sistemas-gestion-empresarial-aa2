from django import forms
from core.models import Cliente
from .models import Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono', 'dni']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if '@empresa.com' not in email:
            raise forms.ValidationError("El email debe ser de dominio corporativo (@empresa.com).")
        return email


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['sku', 'nombre', 'precio_base', 'tipo_iva', 'stock']

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock no puede ser inferior a 0.")
        return stock
