import re

files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

temp = [re.split(r"([0-9]+)", s) for s in files]

print(temp)
