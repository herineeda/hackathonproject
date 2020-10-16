from django.shortcuts import get_object_or_404, render

from cart.forms import AddProductForm

from .models import *


def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True) 
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category) 
        
    return render(request,
                             'shop/list.html', 
                            {
                                'current_category':current_category,
                                'categories':categories,
                                'products':products
                                })


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug) #제품 있으면 불러와짐 
    add_to_cart = AddProductForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product,'add_to_cart':add_to_cart})






