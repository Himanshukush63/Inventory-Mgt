from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'inventory/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'inventory/product_form.html'
    success_url = reverse_lazy('product-list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'inventory/product_confirm_delete.html'
    success_url = reverse_lazy('product-list')

def dashboard(request):
    products = Product.objects.all()
    context = {
        'total_products': products.count(),
        'low_stock': products.filter(stock__lt=5).count(),
        'categories': {
            'mobile': products.filter(category='mobile').count(),
            'laptop': products.filter(category='laptop').count(),
            'smartwatch': products.filter(category='smartwatch').count(),
        }
    }
    return render(request, 'inventory/dashboard.html', context)
