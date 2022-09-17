# Image Processing Mini Problems

This repository will be a collection of mini image processing problems that
serve to aid in my learning and understanding of computer vision.

## Otsu's Method for Computing Threshold Automatically -- otsu.py

Thresholding is a way to separate out shapes in the image based on whether
certain pixels are above or below a threshold for intensity. The method
I implemented here searches for a "good" threshold by maximizing the
inter-class variance between the two groups created by the threshold.
Intuitively, this means that the algorithm selects the threshold at which the
two class created are most different from one another in terms of average pixel
intensity.

One practical application of this algorithm is demonstrated by my example,
separating the subject of a photo from the background. Of course, this is
dependent on the contrast between subject and background, but the technique can
be quite effective.

To run: python3 otsu.py [imageName]

## Histogram Equalization for Pixel Intensity

This algorithm increases contrast near histogram maxima and decreases contrast
near histogram minima. This results in a much more equal histogram of pixel
intensities.

To accomplish this task, I implemented the following transformation:
    $s_k = T(r_k) = \frac{(L - 1)}{M * N}*\Sigma_{j=0}^{k}n_j$
Where:
 - $r \in [0, L - 1]$ represents pixel values (in intensity) with $r = 0$ being black and $r = L - 1$ being white
 - $L$ is the number of distinct pixel values, i.e. 256
 - $M, N$ are the dimensions of the photo
 - $n_k$ is the number of pixels with intensity $r_k$

To run: python3 histEq.py [imageName]
