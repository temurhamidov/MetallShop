from django.contrib import admin
from .models import Category, Type, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'slug', 'created']
    list_filter = ['created']
    search_fields = ['name']

