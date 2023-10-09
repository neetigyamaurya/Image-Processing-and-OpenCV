# Import necessary libraries
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image and resize it
image = cv2.imread('images/ColorWall-lqwzor.jpg')
old_height, old_width = image.shape[:2]
ratio = float(old_width) / float(old_height)
new_height = int(input("Enter new height: "))
new_width = int(new_height * ratio)
print(old_height, old_width)
image = cv2.resize(image, (new_width, new_height))
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Laplacian ------------------------------------------------------------------------
# Apply the Laplacian operator to detect rapid intensity changes (edges) in the image
laplacian = cv2.Laplacian(image, cv2.CV_64F,
                          ksize=1)  # The Laplacian may produce negative values, so we take the absolute
laplacian_abs = np.uint8(np.absolute(laplacian))  # Convert to unsigned 8-bit for display

# Sobel Operations ----
# Apply Sobel operators to detect edges in both horizontal and vertical directions
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # Sobel X for vertical lines
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # Sobel Y for horizontal lines

sobel_x_abs = np.uint8(np.absolute(sobel_x))  # Convert to unsigned 8-bit
sobel_y_abs = np.uint8(np.absolute(sobel_y))  # Convert to unsigned 8-bit

# Combine Sobel results to find edges in both directions
sobel_merged = cv2.bitwise_or(sobel_x_abs, sobel_y_abs)

# Display the original image and the results of Laplacian and Sobel operators
cv2.imshow('image', image)
cv2.imshow('laplacian', laplacian)
cv2.imshow('laplacian_abs', laplacian_abs)
cv2.imshow('sobel_x', sobel_x)
cv2.imshow('sobel_y', sobel_y)
cv2.imshow('sobel_x_abs', sobel_x_abs)
cv2.imshow('sobel_y_abs', sobel_y_abs)
cv2.imshow('sobel_merged', sobel_merged)
titles = ['image', 'laplacian', 'laplacian_abs', 'sobel_x', 'sobel_y', 'sobel_x_abs', 'sobel_y_abs', 'sobel_merged']
images = [image, laplacian, laplacian_abs, sobel_x, sobel_y, sobel_x_abs, sobel_y_abs, sobel_merged]
for i in range(8):
    plt.subplot(4, 2, i + 1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
