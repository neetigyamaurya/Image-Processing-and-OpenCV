"""
Backprojection using Histogram Technique

This code demonstrates backprojection using histogram technique. Backprojection is a method to highlight regions
in an image that have a similar color distribution to a reference image (ROI).

The code performs the following steps:
1. Load an original image and an ROI (Region of Interest) image.
2. Converts both images to the HSV (Hue, Saturation, Value) color space.
3. Calculate the histogram of the ROI image in the HSV color space.
4. Use the histogram to create a mask that highlights areas in the original image with similar color distribution.
5. Applies filtering to remove noise from the mask.
6. Thresholds the mask to create a binary mask.
7. Combines the binary mask with the original image to produce the result.

"""

import cv2


def resize(image):
    """This function returns the resized image while preserving the aspect ratio."""
    height, width = image.shape[:2]
    ratio = float(width) / float(height)
    new_height = int(input("Enter the new Height of the image: "))
    new_width = int(ratio * new_height)
    image = cv2.resize(image, (new_width, new_height))
    return image


# Load the original image
original = cv2.imread('images/bg-sep.jpg')
original = resize(original)
hsv_original = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)

# Load the ROI (Region of Interest) image
roi = cv2.imread("images/roi.jpg")
roi = resize(roi)
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Histogram of the ROI
roi_hist = cv2.calcHist([hsv], [0, 1], None, [100, 256], [0, 180, 0, 256])
mask = cv2.calcBackProject([hsv_original], [0, 1], roi_hist, [0, 180, 0, 256], 1)

# Filtering - Removal of Noise
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
mask = cv2.filter2D(mask, -1, kernel)
_, mask = cv2.threshold(mask, 200, 255, cv2.THRESH_BINARY)
mask = cv2.merge((mask, mask, mask))
result = cv2.bitwise_or(original, mask)

# Display images
cv2.imshow('Original', original)
cv2.imshow('HSV', hsv)
cv2.imshow('Mask', mask)
cv2.imshow('Result', result)

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
