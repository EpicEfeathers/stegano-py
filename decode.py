from PIL import Image
import math

im = Image.open("modified_image.png")

pixels = list(sum(im.getdata(), ()))

binary = [str(pixel & 1) for pixel in pixels]
decoded_binary = [''.join(binary[i:(i+7)]) for i in range(0, len(binary), 7)]

decoded_message = []
for letter in decoded_binary:
    char = chr(int(letter, 2))
    if char == "\x7f":
        break
    decoded_message.append(char)

decoded_message = ''.join(decoded_message)
print(f"Output:\n{decoded_message}")