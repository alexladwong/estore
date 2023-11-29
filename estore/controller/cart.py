from django.http.response import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from django.http import HttpResponseBadRequest, JsonResponse, Http404
from django.db import transaction

from estore.models import Product, Cart

from django.contrib.auth.decorators import login_required


@transaction.atomic
def addtocart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            prod_id = int(request.POST.get("product_id"))
            product_check = Product.objects.filter(id=prod_id).first()

            if product_check:
                prod_qty = int(request.POST.get("product_qty"))

                if Cart.objects.filter(
                    user=request.user.id, product_id=prod_id
                ).exists():
                    return JsonResponse(
                        {"success": False, "messages": "Product already in the cart!"}
                    )
                else:
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(
                            user=request.user, product_id=prod_id, product_qty=prod_qty
                        )
                        return JsonResponse(
                            {
                                "success": False,
                                "message": "Product added successfully!",
                            }
                        )
                    else:
                        return JsonResponse(
                            {
                                "success": False,
                                "message": "Only "
                                + str(product_check.quantity)
                                + " available at the moment",
                            }
                        )
            else:
                return JsonResponse(
                    {
                        "success": False,
                        "message": "No Such Item Found. Check again later",
                    }
                )
        else:
            return JsonResponse({"success": True, "message": "Login to Continue"})

    return JsonResponse({"success": False, "message": "Invalid Request"})


# @login_required
def viewcart(request):
    if request.user.is_authenticated:
        viewcart = Cart.objects.filter(user=request.user)
        context = {"cart": viewcart}
        return render(request, "cart.html", context)
    else:
        # If the user is not authenticated, you can redirect them to the login page
        return redirect("/login")


# Replace with the actual login URL


# @login_required TOTAL LOCKOUT
# def viewcart(request):
#     if request.user.is_authenticated:
#         cart = Cart.objects.filter(user=request.user)
#         context = {"cart": cart}
#         return render(request, "cart.html", context)


def updatecart(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        prod_qty = int(request.POST.get("product_qty"))

        # Try to get the cart item for the given product and user
        try:
            cart = Cart.objects.get(user=request.user, product_id=prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse(
                {"success": True, "message": "Cart Updated Successfully!"}
            )
        except Cart.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "Product not found in the cart."}
            )

    return JsonResponse({"success": False, "message": "Invalid Request"})


# from django.http import JsonResponse


# from django.http import JsonResponse, HttpResponseBadRequest
# from django.shortcuts import redirect
# from your_app.models import Cart


def deletecartitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get("product_id"))
        try:
            cart_item = Cart.objects.get(user=request.user, product_id=prod_id)
            cart_item.delete()
            return JsonResponse({"success": True, "message": "Deleted Successfully!"})
        except Cart.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "Item not found in the cart."}
            )
    else:
        return HttpResponseBadRequest("Invalid request method")


# Use a URL pattern to map this view to a specific URL.


#
#
#
# OLD ADD TO CART FUNCTIONS


# def addtocart(request):
#     if request.method == "POST":
#         if request.user.is_authenticated:
#             prod_id = int(request.POST.get("product_id"))
#             product_check = Product.objects.get(id=prod_id)
#             if product_check:
#                 if Cart.objects.filter(user=request.user.id, product_id=prod_id):
#                     return JsonResponse({"status": "Product Aready in Cart!"})
#                 else:
#                     prod_qty = int(request.POST.get("product_qty"))

#                     if product_check.quantity >= prod_qty:
#                         Cart.objects.create(
#                             user=request.user, product_id=prod_id, product_qty=prod_qty
#                         )
#                         return JsonResponse({"status": "Product added Successfully!"})
#                     else:
#                         return JsonResponse(
#                             {
#                                 "status": "Only "
#                                 + str(product_check.quantity)
#                                 + " Available at the moment"
#                             }
#                         )

#             else:
#                 return JsonResponse(
#                     {"status": "No such Product Found, please check again later"}
#                 )

#         else:
#             return JsonResponse({"status": "Login to Continue"})
#     return redirect("/")
