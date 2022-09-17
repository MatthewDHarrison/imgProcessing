# histogram equalization
from PIL import Image
import numpy as np
import sys
import matplotlib.pyplot as plt

figure, ax = plt.subplots(2, 2)
M = 400
N = 300

if len(sys.argv) > 1:
    image = Image.open(sys.argv[1])
else:
    image = Image.open('kdot.jpg')
res_image = image.resize((M,N)).convert('L')
res_image.show()

im = np.array(res_image, dtype=np.uint8)
flatIm = im.flatten()
print(len(flatIm))

# array of number of pixels with gray value = index
n = np.zeros(256)
for i in range(0, len(flatIm)):
    n[flatIm[i]] += 1

print(n)
ax[0][0].hist(flatIm, np.arange(0, 256))
ax[0][0].set_title("Histogram of Pixel Values")

C = 255 / (N * M)
print("C is ", C)
im_copy = im.copy()
im_histEq = im.copy()
im_histEq_c = im.copy()

T = np.zeros(256)
T_c = np.zeros(256)
g = 0.5
for k in range(0,256):
    # where pixel intesntiy = k, replace with C * sum from 0 to i of n
    # to constrain slope, find distance between T[k] and k, subtract dist * g,
    # where g is some fraction penalty
    T[k] = round(C * np.sum(n[0:k+1]))
    print("Sum is ", np.sum(n[0:k+1]))
    print(k, T[k])
    im_histEq[im == k] = T[k]
    T_c[k] = T[k] - g * (T[k] - k)
    im_histEq_c[im == k] = T_c[k]

ax[0][1].plot(np.arange(0, 256), T)
ax[0][1].set_title("Plot of T(r)")
ax[1][1].plot(np.arange(0, 256), T_c)
ax[1][1].set_title("Plot of T(r) w/ Constrained Slope")


ax[1][0].hist(im_histEq.flatten(), np.arange(0, 256))
ax[1][0].set_title("Histogram of Pixel Values After Equalization")
plt.show()

image_histEq = Image.fromarray(im_histEq)
image_histEq.show()
image_histEq_c = Image.fromarray(im_histEq_c)
image_histEq_c.show()
