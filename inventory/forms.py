from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'brand', 'model_number', 'price', 'stock', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
