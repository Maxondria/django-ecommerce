from django.shortcuts import redirect, render

from products.models import Product

from .models import Cart


def cart_home(request):
    cart, _is_new_cart = Cart.objects.new_or_get(request)

    return render(request, "carts/home.html", {"cart": cart})


def cart_update(request):
    product_id = request.POST.get("product_id")
    if product_id:
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            # TODO: Show message to user!
            return redirect("cart:home")

        cart, is_new_cart = Cart.objects.new_or_get(request)
        if product in cart.products.all():
            cart.products.remove(product)
        else:
            cart.products.add(product)
        request.session['cart_total_items'] = cart.products.count()
    return redirect("carts:home")
