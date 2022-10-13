from django import forms
from .models import CarrinhoCompra


class CarrinhoCompra2(forms.ModelForm):
    class Meta:
        model = CarrinhoCompra
        fields = '__all__'
