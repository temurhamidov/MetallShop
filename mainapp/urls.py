from django.urls import path
from .views import HomeView, AboutView, ProductsView, ProductListWithType

app_name = 'mainapp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<slug:slug>', ProductListWithType.as_view(), name='products_type'),
]