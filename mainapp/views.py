from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from .models import Type

class HomeView(ListView):
    model = Type
    context_object_name = 'types'
    template_name = 'mainapp/home.html'
