from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock']
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list') 

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['name', 'description', 'price', 'stock']
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list') 

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list') 
