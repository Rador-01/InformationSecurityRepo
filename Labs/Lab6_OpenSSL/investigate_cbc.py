from PIL import Image
from random import randrange

width = 432
height = 475

with open("classified_cbc.enc", "rb") as file:
    data = file.read()

#exclude the header and encrypted padding
ciphertext = data[16:16 + width * height]

shades = {}
pixels = []

for i in range(0, len(ciphertext), 16):
    block = ciphertext[i:i + 16]

    if block not in shades:
        shades[block] = randrange(256)

    pixels.extend([shades[block]] * 16)

image = Image.frombytes("L", (width, height), bytes(pixels))
image.save("pattern_cbc.png")

total = len(ciphertext) // 16

print("Total blocks:", total)
print("Distinct blocks:", len(shades))
print("Repeated occurrences:", total - len(shades))