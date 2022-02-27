from PIL import Image
from numpy import asarray
import random

image = Image.open('danger_zone.png')

array = asarray(image)
#print(array)

wight, height = image.size
#print(wight, height)

execution = 100000
size_red = 0
size_blue = 0

for _ in range(execution):
	h = random.randint(0, height - 1)
	w = random.randint(0, wight - 1)
	if(array[h][w][0] == 255):
		size_red += 1
	else:
		size_blue += 1

Area = (size_red / (size_blue + size_red) * 42)
print(Area)