import cv2
import numpy as np

# Create a 5x5 kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)

# Load an image
image = cv2.imread('images/cupped-hand-gesture-sharing-caring.jpg')
height, width = image.shape[:2]

# Calculate the aspect ratio to maintain proportions when resizing
ratio = float(width) / float(height)

# Ask the user to input the new height for the image
new_height = int(input("Enter the new height: "))

# Calculate the new width using the aspect ratio
new_width = int(ratio * new_height)

# Resize the image to the new dimensions
image = cv2.resize(image, (new_width, new_height))
image_1 = image

# Convert the resized image to grayscale
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)

# Apply median blur to reduce noise
blur = cv2.medianBlur(image_1, 5)

# Apply binary inversion thresholding
ret, thresh = cv2.threshold(blur, 230, 255, cv2.THRESH_BINARY_INV)

# Dilate the thresholded image using the kernel
thresh = cv2.dilate(thresh, kernel)

# Find contours in the thresholded image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Print the contours and their count
print("Contours:", contours)
print("Number of Contours:", len(contours))

# Loop over the contours
for c in contours:
    # Calculate epsilon for contour approximation
    epsilon = 0.00001 * cv2.arcLength(c, True)

    # Approximate the contour with fewer vertices
    data = cv2.approxPolyDP(c, epsilon, True)

    # Calculate the convex hull of the approximated contour
    hull = cv2.convexHull(data)

    # Draw the original contour in green and the convex hull in black
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.drawContours(image, [hull], -1, (0, 0, 0), 5)

# Find convexity defects
hull_2 = cv2.convexHull(contours[0], returnPoints=False)
defect = cv2.convexityDefects(contours[0], hull_2)

# Print information about convexity defects
print("Convexity Defects:", defect)
print("Shape of Defect:", defect.shape)
print("Number of Defects:", defect.shape[0])

# Loop over convexity defects
for i in range(defect.shape[0]):
    start_point, end_point, farthest_point, damaged_point = defect[i, 0]

    # Get coordinates of points related to the defect
    start = tuple(c[start_point][0])
    end = tuple(c[end_point][0])
    far = tuple(c[farthest_point][0])

    # Draw a circle at the farthest point of the defect in blue
    cv2.circle(image, far, 5, [255, 0, 0], -1)

# Find the extreme points of the largest contour
c_max = max(contours, key=cv2.contourArea)

# Determine the most extreme points along the contour
extreme_left = tuple(c_max[c_max[:, :, 0].argmin()][0])
extreme_right = tuple(c_max[c_max[:, :, 0].argmax()][0])
extreme_top = tuple(c_max[c_max[:, :, 1].argmin()][0])
extreme_bottom = tuple(c_max[c_max[:, :, 1].argmax()][0])

# Draw circles at the extreme points with different colors
cv2.circle(image, extreme_left, 8, (255, 0, 255), -1)  # Pink
cv2.circle(image, extreme_right, 8, (0, 125, 255), -1)  # Brown
cv2.circle(image, extreme_top, 8, (255, 10, 0), -1)  # Blue
cv2.circle(image, extreme_bottom, 8, (19, 152, 152), -1)  # Green

# Display the images
cv2.imshow('image', image)
cv2.imshow('thresh', thresh)

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
