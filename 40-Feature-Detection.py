"""Feature and Corner Detection
"""
import cv2  # This helps us work with pictures
import numpy as np

# --------------------------------Harris Corner Detection---------------------------------------------------------------
"""OpenCV has the function cv2.cornerHarris() for this purpose . Its arguments are
image- Should be grayscale and float32 type.
blocksize- It is the size of neighbourhood considered for corner detection
k- Harris detector free parameter in the equation"""


# Function to resize the image while keeping its shape
# Imagine making a big picture smaller
def resize(image, new_height):
    # Figure out how wide the picture should be to keep it looking nice
    h, w = image.shape[:2]  # This tells us the picture's height and width
    ratio = float(w) / float(h)  # Imagine the picture's width compared to its height
    new_width = int(ratio * new_height)  # This is how wide the picture should be
    resized_image = cv2.resize(image, (new_width, new_height))  # Make the picture the right size
    return resized_image  # Get the new, smaller picture


# Load the image (a picture of a car) and make it a bit smaller
image = cv2.imread('images/shapes.jpg')  # Get the picture
image = resize(image, 800)  # Make it a good size for us to work with
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

# Detect Corner
res = cv2.cornerHarris(gray, 2, 3, 0.04)
kernel_dil = np.ones((2, 2), np.uint8)
res = cv2.dilate(res, kernel_dil)
image[res > 0.01 * res.max()] = [0, 0, 255]  # Marked Color

# ------------------------------------------Shi-Tomasi Corner Detection-------------------------------------------------
"""It is more effective approach compared to Harris corner detector. In this we limits the number of corners and corners
quality. It is more user friendly. Image MUST BE IN GRAY. CORNERS MUST BE IN INT64 type"""
copy = image
gray_copy = cv2.cvtColor(copy, cv2.COLOR_BGR2GRAY)
corners = cv2.goodFeaturesToTrack(gray_copy, 10, 0.01, 20)
corners = np.int64(corners)

for i in corners:
    x, y = i.ravel()
    print(x, y)
    cv2.circle(copy, (x, y), 3, (255, 255, 255), -1)
cv2.imshow("Harris Corner Detection", image)
# cv2.imshow("Grayscale Image", gray)
cv2.imshow("Shi-Tomasi Corner Detection", copy)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
