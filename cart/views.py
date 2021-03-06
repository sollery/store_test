import json
from django.contrib.messages.storage import session
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm



# @require_POST
# def cart_add(request, id):
#     cart = Cart(request)
#     product = get_object_or_404(Product, id=id)
#     form = CartAddProductForm(request.POST)
#     if form.is_valid():
#         cd = form.cleaned_data
#         cart.add(product=product,
#                  quantity=cd['quantity'])
#         return redirect('cart_detail')
# def cart_remove(request, product_id):
#
#         # cart = Cart(request)
#         # product = get_object_or_404(Product, pk=product_id)
#         # cart.remove(product)
#     return render(request, 'detail.html')


# def cart_detail(request):
#     cart = Cart(request)
#     if request.method == 'POST':
#         temp = json.load(request)
#         product = get_object_or_404(Product, pk=temp['product_id'])
#         cart.remove(product)
#         new_cart = Cart(request)
#         print(temp)
#         print(new_cart.cart)
#         return HttpResponse(json.dumps(new_cart.cart))
#     return render(request, 'detail.html', {'cart': cart})


def cart_change(request):
    cart = Cart(request)
    if request.method == 'POST':
        temp = json.load(request)
        product = get_object_or_404(Product, pk=temp['product_id'])
        if temp['change'] == 'plus':
            cart.plus(product)
        elif temp['change'] == 'minus':
            cart.minus(product)
        elif temp['change'] == 'del':
            cart.remove(product)
        elif temp['change'] == 'add':
            print('111111111111')
            cart.add(product=product)

        cart = Cart(request)
        print(temp)
        print(cart.cart)
        return HttpResponse(json.dumps(cart.cart))
    return render(request, 'detail.html', {'cart': cart})



