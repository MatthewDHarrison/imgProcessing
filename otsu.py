# Otsu's thresholding
from PIL import Image
import numpy as np
import sys

if len(sys.argv) > 1:
    image = Image.open(sys.argv[1])
else:
    image = Image.open('kdot.jpg')
res_image = image.resize((400,300))

im = np.array(res_image.convert('L'), dtype=np.uint8)
flatIm = im.flatten()
print(type(im))
prevVar = 0
bestThresh = 0

for t in range(0, 255):
    im_group0 = flatIm[np.where(flatIm < t)]
    im_group1 = flatIm[np.where(flatIm >= t)]
    p0 = len(im_group0) / len(flatIm)
    p1 = len(im_group1) / len(flatIm)
    mu0 = np.mean(im_group0)
    mu1 = np.mean(im_group1)

    variance = p0 * p1 * (mu0-mu1)**2
    if variance > prevVar:
        prevVar = variance
        bestThresh = t

im_thresh = np.where(im > bestThresh, 255, 0).astype('uint8')
print(type(im_thresh[0][0]))
image_otsu = Image.fromarray(im_thresh)
image_otsu.show()
