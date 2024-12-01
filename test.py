from PIL import Image

im = Image.open("images/random.png")

print(list(im.load()))