"""
Hough Transformation

Hough's transformation is a technique used to detect shapes in an image if the shape can be represented mathematically.
It can even detect shapes that are broken or distorted to some extent.

This code demonstrates two methods of Hough transformation:
1. cv2.HoughLines(): This method is used to detect lines in an image.
2. cv2.HoughLinesP(): This method is used for probabilistic Hough line transformation.

The code performs the following steps:
1. Load an image and resize it to the desired height.
2. Convert the image to grayscale and apply edge detection.
3. Apply the cv2.HoughLines() method to detect lines in the image and draw them.
4. Apply the cv2.HoughLinesP() method for probabilistic Hough line transformation and draw the lines.
5. Display the image with detected lines.

"""

import cv2
import numpy as np


def resize(image, new_height):
    """This function returns the resized image while preserving the aspect ratio."""
    h, w = image.shape[:2]
    ratio = float(w) / float(h)
    new_width = int(ratio * new_height)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image


# Load and resize the image
image = cv2.imread('images/chessboard.jpg')
new_height = int(input("Enter the new Height of the image: "))
image = resize(image, new_height)

# Convert the image to grayscale and perform edge detection
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
edges = cv2.Canny(opening, 20, 255)

# Detect lines using cv2.HoughLines()
lines = cv2.HoughLines(edges, 1, np.pi / 180, 200)
for rho, theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x_0 = a * rho
    y_0 = b * rho
    x_1 = int(x_0 + 1000 * (-b))
    y_1 = int(y_0 + 1000 * a)
    x_2 = int(x_0 - 1000 * (-b))
    y_2 = int(y_0 - 1000 * a)
    cv2.line(image, (x_1, y_1), (x_2, y_2), (0, 255, 0), 10)

# Detect lines using cv2.HoughLinesP()
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 250, minLineLength=1, maxLineGap=1000)
for line in lines:
    x_1, y_1, x_2, y_2 = line[0]
    cv2.line(image, (x_1, y_1), (x_2, y_2), (0, 0, 255), 5)

# Display the images
cv2.imshow('edges', edges)
cv2.imshow('image', image)
cv2.imshow("Thresh", thresh)

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
