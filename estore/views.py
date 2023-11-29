from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


# Create your views here.
def home(request):
    return render(request, "index.html")  # estore can be removed


def collections(request):
    category = Category.objects.filter(status=0)
    context = {"category": category}
    return render(request, "collections.html", context)


@login_required
def cart(request):
    cart = Cart.objects.filter(user=request.user)

    context = {"cart": cart}

    return redirect(request, "login.html", context)
    LOGIN_URL = "accounts:login"


def collectionsview(request, slug):
    if Category.objects.filter(slug=slug, status=0):
        products = Product.objects.filter(category__slug=slug)

        category = Category.objects.filter(slug=slug).first()
        context = {"products": products, "category": category}
        return render(request, "estore/products/index.html", context)
    else:
        messages.warning(request, "Category not found please try again later")
        return redirect("collections")


def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {"products": products}

        else:
            messages.error(request, "Product not found please try again later")
            return redirect("collections")

    else:
        messages.error(request, "Category not found please try again later")
        return redirect("collections")

    return render(request, "estore/products/view.html", context)
