from django.urls import path
from . import views

from estore.controller import authview, cart

urlpatterns = [
    path("", views.home, name="home"),
    path("collections", views.collections, name="collections"),
    path("cart", views.cart, name="cart"),
    path("collections/<str:slug>", views.collectionsview, name="collectionsview"),
    path(
        "collections<str:cate_slug>/<str:prod_slug>",
        views.productview,
        name="productview",
    ),
    path("register", authview.register, name="register"),
    path("login", authview.loginpage, name="loginpage"),
    path("logout", authview.logoutpage, name="logout"),
    # Add to cart
    path("add-to-cart", cart.addtocart, name="add-to-cart"),
    path("viewcart", cart.viewcart, name="viewcart"),
    # path("viewcart/", cart.viewcart, name="viewcart"),
    path("update-cart", cart.updatecart, name="updatecart"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),
]
