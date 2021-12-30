from django.shortcuts import render, get_object_or_404
from carts.models import CartItem
from carts.views import _cart_id
from category.models import Category
from store.models import Product


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None :
        categories = get_object_or_404(Category, category_slug=category_slug)
        products = Product.objects.all().filter(category=categories, product_is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(product_is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__category_slug=category_slug, product_slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    context = {
        'single_product': single_product,
        'in_cart': in_cart
    }
    return render(request, 'product-detail.html', context)