"""# Morphological Transformations
# They are some simple operations performed on images helps in fixing images
# Performed on Binary Images
# Two transformations 1) Erosion 2) Dilation
# -------------------------------------------Erosion--------------------------------------------------------------------
# It erodes away the boundaries of the foreground objects
# Morphological transformation me background black nhi hona chaiye

Certainly! Here's an explanation of morphological transformations, erosion, and dilation along with some theory:

Morphological Transformations are a set of simple operations performed on binary images (images with pixel values of
either 0 or 255) that help in processing and analyzing shapes within images. These operations are particularly useful
for tasks like noise removal, object detection, and boundary extraction. Two fundamental morphological transformations
are erosion and dilation.

Erosion is a morphological operation that is used to erode away the boundaries of the foreground objects in a binary
image. The key idea is that it "shrinks" the white regions (foreground) by removing pixels from their boundaries.
Erosion is performed using a small kernel, which is a small matrix-like structure that slides over the image. For each
pixel in the image, if all the pixels in the kernel are white (255), the pixel remains white; otherwise, it becomes
black (0).

Erosion is often used to remove small white noises or detach connected objects. However, it should be noted that
repeated erosion may cause the foreground objects to become smaller and may eventually disappear.

Dilation is the opposite of erosion. It is used to expand or "grow" the white regions in a binary image.
Like erosion, dilation also uses a kernel. For each pixel in the image, if any of the pixels in the kernel are
white, the pixel becomes white; otherwise, it remains black.

Dilation is often used to close small black holes within the white regions or to join nearby white regions into a
single connected component. It is commonly used after erosion to restore the size and shape of objects that may
have been eroded away.

Code Explanation
In the provided code:

An image is loaded, converted to grayscale, and resized.
A binary mask is created by thresholding the grayscale image, where pixels with values above 240 become white (255)
and others become black (0).
A kernel is defined for morphological operations.
Erosion is applied to the binary mask using the cv2.erode() function. This shrinks the white regions in the mask.
Dilation is applied to the binary mask using the cv2.dilate() function. This enlarges the white regions.
The code then displays the original image, the binary mask, the result of erosion, and the result of dilation for
visualization purposes.

These morphological transformations are essential tools in image processing, particularly for cleaning up noisy images,
 extracting features, and preparing images for further analysis or object detection tasks."""
# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image, convert it to grayscale, and resize it
image = cv2.imread('2704.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (900, 900))

# Threshold the image to create a binary mask
_, mask = cv2.threshold(image, 240, 255, cv2.THRESH_BINARY_INV)

# Create a kernel for morphological operations (used for both erosion and dilation)
kernel = np.ones((5, 5), np.uint8)

# -------------------------------------------Erosion--------------------------------------------------------------------
# Erosion is used to erode away the boundaries of the foreground objects
# It is applied to binary images, where the background should be black (0) and the foreground should be white (255)
erode = cv2.erode(mask, kernel)

# ------------------------------------------DILATION--------------------------------------------------------------------
# Dilation is the opposite of erosion, and it increases the white region in the image
# It is often used for noise removal because erosion may shrink the foreground
dilation_kernel = np.ones((3, 3), np.uint8)
dilation = cv2.dilate(mask, dilation_kernel)

# Display the original image and the results of erosion and dilation
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.imshow('erode', erode)
cv2.imshow('dilation', dilation)

# Titles for displayed images
titles = ['image', 'mask', 'erode', 'dilation']
images = [image, mask, erode, dilation]

# Display images using Matplotlib
for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
