# Image Histogram - Find, Plot, and Analyze
# This code calculates and plots histograms of an image to analyze its intensity distribution.
# The x-axis represents the range of color values, and the y-axis represents the number of pixels in the image.
# Histograms can help extract information about contrast, brightness, and intensity.

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load an image
image = cv2.imread('images/ColorWall-dp3lzm.jpg')
height, width = image.shape[:2]

# Calculate the aspect ratio to maintain proportions when resizing
ratio = float(width) / float(height)

# Ask the user to input the new height for the image
new_height = int(input("Enter the new height: "))

# Calculate the new width using the aspect ratio
new_width = int(ratio * new_height)

# Resize the image to the new dimensions
image = cv2.resize(image, (new_width, new_height))

# Split the image into its RGB channels
b, g, r = cv2.split(image)

# Calculate histograms for each color channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms using Matplotlib
plt.hist(b.ravel(), 256, (0, 256), color='blue', alpha=0.5, label='Blue Channel')
plt.hist(g.ravel(), 256, (0, 256), color='green', alpha=0.5, label='Green Channel')
plt.hist(r.ravel(), 256, (0, 256), color='red', alpha=0.5, label='Red Channel')
plt.title("Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# Display the original image and individual color channels
cv2.imshow("Image", image)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)

# Convert the image to grayscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Calculate a histogram for the grayscale image
hist = cv2.calcHist([image], [0], None, [256], [0, 255])

# Plot the grayscale histogram
plt.plot(hist)
plt.title("Grayscale Histogram")
plt.show()

# Histogram equalization is good when the intensity of the image is confined to a particular region.
# It accepts a grayscale image.
equ = cv2.equalizeHist(image)
res = np.hstack((image, equ))  # Join the original image and the equalized image for comparison
cv2.imshow("Equalized Histogram", res)
hist = cv2.calcHist([equ], [0], None, [256], [0, 256])
plt.plot(hist)
plt.title("Equalized Histogram")
plt.show()

# Contrast Limited Adaptive Histogram Equalization (CLAHE)
# Creates a CLAHE object (Arguments are optional)
# It is used to enhance image and also handle noise from an image region.
# A grayscale image is required.
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))  # Keep the clipLimit between 1 and two for better results.
cl1 = clahe.apply(image)
cv2.imshow("CLAHE", cl1)
hist = cv2.calcHist([cl1], [0], None, [256], [0, 256])
res = np.hstack((image, equ, cl1))  # Join the original image, equalized, and CLAHE-processed images
plt.plot(hist)
plt.title("CLAHE")
plt.show()
cv2.imshow("Comparison", res)

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
