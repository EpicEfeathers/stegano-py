from PIL import Image

im = Image.open("images/random.png")

width, height = im.size
im_pixels = im.load()

input = input("Message: ")

text_binary = [format(ord(char), '07b') for char in input]


bits = ''.join(text_binary) + "1111111"

pixels = list(sum(im.getdata(), ()))

for i, pixel in enumerate(pixels):
    if i == len(bits):
        break
    if int(bits[i]) & 1:
        if not pixel & 1:
            pixels[i] = (pixel + 1)
        else:
            pixels[i] = (pixel)
    else:
        if pixel & 1:
            pixels[i] = (pixel - 1)
        else:
            pixels[i] = (pixel)


pixels = [(pixels[i], pixels[i+1], pixels[i+2]) for i in range(0, len(pixels), 3)]
print(pixels)

i = 0
for h in range(height):
    for w in range(width):
        im_pixels[w,h] = pixels[i]
        i+=1

#print(pixels)


im.save("modified_image.png")