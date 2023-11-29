from PIL import Image, __version__

print(f"Pillow version: {__version__}")


def resize_image(image, width=500, height=500):
    try:
        img = Image.open(image)
        img = img.resize((width, height), Image.ANTIALIAS)
        img.save(image.path)
        print(f"Image resized successfully to {width}x{height}")
    except Exception as e:
        print(f"Error: {e}")
