import pdb

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.base import View

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Order, OrderItem, OrderTransaction


# 주문하기 누르면 첫페이지
def order_create(request):
    # 장바구니에 존재하는 상품 정보 받아오기
    cart = Cart(request)
    # 주문 정보가 입력 완료된 상황(결제 폼 작성 완료하여 POST 형태로 request를 받은 상황)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # 작성한 폼 validation 진행
        if form.is_valid():
            order = form.save()
            for item in cart:
                # 장바구니에 들어있는 모든 상품 정보를 OrderItem 모델에 저장
                OrderItem.objects.create(
                    order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return render(request, 'order/created.html', {'order': order})
    # 주문 정보가 입력되지 않은 상황(처음 결제페이지로 이동한 상황)
    else:
        form = OrderCreateForm()

    return render(request, 'order/order_create.html', {'form': form})


class OrderCreateAjaxView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        form = OrderCreateForm(request.POST)

        if form.is_valid():
            order = form.save()
            # 쿠폰은 제거

            for item in cart:
                # 장바구니에 들어있는 모든 상품 정보를 OrderItem 모델에 저장
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()

            # data 응답
            data = {
                "order_id": order.id
            }
            return JsonResponse(data)
        return JsonResponse({}, status=401)


class OrderCheckoutAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인 안 했을 때
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)
        amount = request.POST.get('amount')

        # try:
        merchant_order_id = OrderTransaction.objects.create_new(
            order=order,
            amount=amount
        )
        # except:
        # merchant_order_id = None
        print(merchant_order_id)
        if merchant_order_id is not None:
            data = {
                "works": True,
                "merchant_id": merchant_order_id
            }
            return JsonResponse(data, status=200)
        else:
            return JsonResponse({}, status=401)


class OrderImpAjaxView(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:  # 로그인 안 했을 때
            return JsonResponse({"authenticated": False}, status=403)

        order_id = request.POST.get('order_id')
        order = Order.objects.get(id=order_id)

        merchant_id = request.POST.get('merchant_id')
        imp_id = request.POST.get('imp_id')
        amount = request.POST.get('amount')

        try:
            trans = OrderTransaction.objects.get(
                order=order_id,
                merchant_order_id=merchant_id,
                amount=amount
            )
        except:
            trans = None
        if trans is not None:
            trans.transaction_id = imp_id
            trans.success = True
            trans.save()
            order.paid = True
            order.save()

            data = {
                "works": True
            }
            return JsonResponse(data)

        else:
            return JsonResponse({}, status=401)


def order_complete(request):
    order_id = request.GET.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    return render(request, 'order/created.html', {'order': order})
