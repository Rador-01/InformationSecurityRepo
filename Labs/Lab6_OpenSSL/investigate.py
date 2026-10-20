from PIL import Image

width = 432
height = 475

with open("classified.enc", "rb") as file:
    data = file.read()

# Exclude the header and encrypted padding
ciphertext = data[16:16 + width * height]

shades = {}
pixels = []

for i in range(0, len(ciphertext), 16):
    block = ciphertext[i:i + 16]

    if block not in shades:
        shades[block] = (len(shades) * 73) % 256

    pixels.extend([shades[block]] * 16)

image = Image.frombytes("L", (width, height), bytes(pixels))
image.save("pattern_ecb.png")