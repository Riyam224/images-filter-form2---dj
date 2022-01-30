from django import forms
from django.forms.widgets import Media
from .models import Product



class ProductForm(forms.ModelForm):
    """Form definition for Product."""

    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = ['name' , 'desc' , 'image']
