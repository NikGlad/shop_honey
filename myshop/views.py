from django.shortcuts import render, get_object_or_404

import cart.cart
from .models import Product
from cart.forms import CartAddProductForm


def product_list(request):
    products = Product.objects.filter(available=True)

    return render(request, 'shop/product/list.html',
                  {
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        })

def about(request):
    return render(request, "about_us/about.html")

def contacts(request):
    return render(request, "contacts/contacts.html")
