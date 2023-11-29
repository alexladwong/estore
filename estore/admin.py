from django.contrib import admin

from .models import *
from .resize_image import resize_image


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "name",
        "small_description",
        "description",
        "meta_title",
        "meta_keywords",
    )
    search_fields = (
        "description",
        "meta_title",
        "meta_keywords",
        "price",
    )


class ImageSizeAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if (
            "image" in form.changed_data
        ):  # Replace 'image' with the name of your image field
            resize_image(obj.image)  # Replace 'image' with the name of your image field
        super().save_model(request, obj, form, change)


admin.site.register(ImageSize)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
