# histogram equalization
from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt

figure, (ax0, ax1) = plt.subplots(2, 1)
print(ax0)
if len(sys.argv) > 1:
    image = Image.open(sys.argv[1])
else:
    image = Image.open('kdot.jpg')
res_image = image.resize((400,300)).convert('L')
res_image.show()

im = np.array(res_image, dtype=np.uint8)
print(im.shape)
flatIm = im.flatten()
print(type(im))

# array of number of pixels with gray value = index
n = np.zeros(256)
for i in range(0, len(flatIm)):
    n[flatIm[i]] += 1
print(n)
ax0.hist(flatIm, np.arange(0, 256))
ax0.set_title("Histogram of Pixel Values")

C = 255 / (300 * 400)
im_copy = im.copy()
T = np.zeros(256)

for k in range(0,256):
    # where pixel intesntiy = k, replace with C * sum from 0 to i of n
    im_copy[im_copy == k] = C * np.sum(n[0:k])
    T[k] = C * np.sum(n[0:k])

ax1.plot(np.arange(0, 256), T)
ax1.set_title("Plot of T(r)")

plt.show()
image_histEq = Image.fromarray(im_copy)
image_histEq.show()
