from .models import Category, Type

def category_list(request):
    categories = Category.objects.all()
    return {'categories' : categories}

def type_list(request):
    types = Type.objects.all()
    return {'types' : types}

