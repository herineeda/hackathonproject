from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .forms import AddProductForm
from .cart import Cart

@require_POST 
#담는기능 
def add(request, product_id): 
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)

    form = AddProductForm(request.POST)

    if form.is_valid(): 

        cd = form.cleaned_data

        cart.add(product=product, quantity=cd['quantity'], is_update=cd['is_update'])

    return redirect('cart:detail')

def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')


def detail(request):
    # 장바구니에 담겨 있는 제품 목록 띄우기, 제품 수량 수정, 지우기, 장바구니 비우기 버튼 구현
    cart = Cart(request)

    for product in cart:

        product['quantity_form'] = AddProductForm(
            initial={'quantity':product['quantity'],
             'is_update':True})
    
    return render(request, 'cart/detail.html', {'cart':cart})