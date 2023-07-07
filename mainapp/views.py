from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView, TemplateView
from .models import Type, Product

class HomeView(TemplateView):
    template_name = 'mainapp/home.html'


class AboutView(TemplateView):
    template_name = 'mainapp/about.html'



class ProductsView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'mainapp/products.html'


class ProductListWithType(View):
    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        products = Product.objects.filter(type__slug=slug)
        context = {
            'products': products,
        }
        return render(request, 'mainapp/products.html', context)