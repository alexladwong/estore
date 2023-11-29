"use strict";
$(document).ready(function () {
  $(".inrement-btn").click(function (e) {
    e.preventDefault();

    var inc_value = $(this).closest(".product-data").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product-data").find(".qty-input").val(value);
    }
  });
  $(".decrement-btn").click(function (e) {
    e.preventDefault();

    var dec_value = $(this).closest(".product-data").find(".qty-input").val();
    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".product-data").find(".qty-input").val(value);
    }
  });

  // Add to Cart
  $(".addToCartBtn").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".product-data").find(".prod_id").val();
    var product_qty = $(this).closest(".product-data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        console.log(response);
        alertify.success(response.status);
      },
    });
  });

  // Change Quantity of Cart Items
  $(".changeQuantity").click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest(".product-data").find(".prod_id").val();
    var product_qty = $(this).closest(".product-data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    $.ajax({
      method: "POST",
      url: "/update-cart",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },

      success: function (response) {
        alertify.success(response.status);
      },
      error: function (xhr, status, error) {
        console.log("AJAX Error: " + error);
      },
    });
  });
});

// Delete
$(".delete-cart-item").click(function (e) {
  e.preventDefault();

  var product_id = $(this).closest(".product-data").find(".prod_id").val();
  var product_qty = $(this).closest(".product-data").find(".prod_qty").val();
  var token = $("input[name=csrfmiddlewaretoken]").val();

  $.ajax({
    method: "POST",
    url: "/delete-cart-item",
    data: {
      product_id: product_id,
      product_qty: product_qty,
      csrfmiddlewaretoken: token,
    },
    success: function (response) {
      console.log(response);
      alertify.success(response.messages); // Access "message" property for the success message
      $(".cartdata").load(location.href + " .cartdata");
    },
  });
});
