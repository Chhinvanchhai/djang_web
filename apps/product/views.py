from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'product/product_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product_detail.html'

class ProductCreateView(CreateView):
    # model = Product
    # fields = ['name', 'description', 'price', 'stock', 'category']
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list') 

class ProductUpdateView(UpdateView):
    # model = Product
    # fields = ['name', 'description', 'price', 'stock','category']
    model = Product
    form_class = ProductForm
    template_name = 'product/product_form.html'
    success_url = reverse_lazy('product:product_list') 

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_confirm_delete.html'
    success_url = reverse_lazy('product:product_list') 

# Category secton


class CategoryListView(ListView):
    model = Category
    template_name = 'catergory/category_list.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'catergory/category_detail.html'

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'catergory/category_form.html'
    success_url = reverse_lazy('product:category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'catergory/category_form.html'
    success_url = reverse_lazy('product:category_list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catergory/category_confirm_delete.html'
    success_url = reverse_lazy('product:category_list')