from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from cart.forms import AddProductForm
from .models import *
from .forms import ReviewForm
from django.core.exceptions import PermissionDenied

def product_in_category(request, category_slug=None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display=True)
    if category_slug:
        current_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html', {
        'shop_active': "is-active",
        'current_category': current_category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, product_slug=None):
    product = get_object_or_404(
        Product, id=id, slug=product_slug)  # 제품 있으면 불러와짐
    add_to_cart = AddProductForm(initial={'quantity': 1})
    
    review_form = ReviewForm() # 리뷰를 작성할 폼 가져오기
    return render(request, 'shop/detail.html', {
        'shop_active': "is-active",
        'product': product,
        'add_to_cart': add_to_cart,
        'review_form':review_form
    })

# # 상품 리뷰 달기
def review(request, id, category, product_slug=None):
    form = ReviewForm(request.POST)

    if form.is_valid():
        temp = form.save(commit=False)
        temp.category = Category.objects.get(name=category)
        temp.product =  get_object_or_404(Product, id=id, slug=product_slug)
        temp.writer = request.user
        # temp.rate
        temp.date = timezone.datetime.now()
        temp.save()

        # 리뷰가 작성될 때마다 Product의 리뷰 개수가 증가.
        product = get_object_or_404(Product, id=id, slug=product_slug)
        r_count = int(product.count)
        r_count += 1
        product.count = r_count
        product.save()
        return redirect('shop:product_detail', id, product_slug)

# 리뷰 삭제하기
def delete_review(request, id, category, review_id, product_slug=None):
    my_review = get_object_or_404(Review, pk=review_id)

    if request.user == my_review.writer:
        my_review.delete()

        # 리뷰가 삭제될 때마다 Product의 리뷰 개수가 감소.
        product = get_object_or_404(Product, id=id, slug=product_slug)
        r_count = int(product.count)
        r_count -= 1
        product.count = r_count
        product.save()
        return redirect('shop:product_detail', id, product_slug)

    else:
        raise PermissionDenied