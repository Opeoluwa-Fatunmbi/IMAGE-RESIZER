import os
from PIL import Image

def resize_images(directory, size):
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = Image.open(f"{directory}/{filename}")
            image = image.resize(size)
            image.save(f"{directory}/resized_{filename}")

directory = "/path/to/images"
size = (800, 600)
resize_images(directory, size)
