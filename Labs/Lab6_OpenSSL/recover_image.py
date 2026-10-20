from PIL import Image

with open("recovered.raw", "rb") as file:
    pixels = file.read()

image = Image.frombytes("L", (432, 475), pixels)
image.save("recovered.png")