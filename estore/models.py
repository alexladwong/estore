import os
import datetime
from django.db import models
from django.contrib.auth.models import User

from PIL import Image

from estore.resize_image import resize_image  # Import the Image class from Pillow


# Define the get_file_path function for image uploads
def get_file_path(instance, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join("uploads/", filename)


class Category(models.Model):
    slug = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=False, blank=True)

    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=200, null=False, blank=False)
    meta_keywords = models.CharField(max_length=200, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.name


# New Models Added


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=False, blank=False)
    small_description = models.CharField(max_length=150, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    meta_title = models.CharField(max_length=200, null=False, blank=False)
    meta_keywords = models.CharField(max_length=200, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Define the Cart model with the image field
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="cart_images/")  # Add an image field

    # Override the save method to resize the image before saving
    def save(self, *args, **kwargs):
        if self.image:
            resize_image(self.image)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)


from django.db import models


class ImageSize(models.Model):
    # Your other fields
    image = models.ImageField(upload_to="your_upload_path/")

    def save(self, *args, **kwargs):
        if "image" in self.__dict__ and hasattr(self.image, "path"):
            resize_image(self.image)  # Resize the image
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.image)


# class WholeSaleProductOrders(models.Model):
#     STATUS_CHOICES = (
#         ("Accepted", "Accepted"),
#         ("Packed", "Packed"),
#         ("On The Way", "On The Way"),
#         ("Delivered", "Delivered"),
#         ("Cancel", "Cancel"),
#     )


#     order_id = models.CharField(max_length=50, default="")
#     user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
#     products = models.CharField(max_length=50)
#     status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="")


# class dow(models.Model):
#     product = models.OneToOneField(
#         Product,
#         default="",
#         verbose_name="Product Id",
#         on_delete=models.CASCADE,
#         null=True,
#     )
#     price = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.product}"


# class trend(models.Model):
#     product = models.OneToOneField(
#         Product, default="", on_delete=models.CASCADE, null=True
#     )
#     number = models.PositiveIntegerField()

#     def __str__(self):
#         return f"{self.product}"


# class MyCart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product_id = models.CharField(max_length=100)
#     number = models.PositiveIntegerField(default=0)


# class Orders(models.Model):
#     STATUS_CHOICES = (
#         ("Accepted", "Accepted"),
#         ("Packed", "Packed"),
#         ("On The Way", "On The Way"),
#         ("Delivered", "Delivered"),
#         ("Cancel", "Cancel"),
#     )
#     order_id = models.CharField(max_length=50, default="")
#     saler = models.CharField(
#         max_length=100,
#         default="ladwong@admin",
#     )
#     user = models.ForeignKey(User, default="", on_delete=models.CASCADE)
#     products = models.CharField(max_length=50)
#     size = models.CharField(max_length=50, default="", null=True)
#     status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="")
