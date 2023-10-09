"""Certainly! Let's add comments and explanations for the lines where `c_x` and `c_y` are calculated:

```Python
# Loop over the contours
for c in contours:
    # Compute the moments of the contour using image moments
    M = cv2.moments(c)

    # Calculate the x-coordinate of the center of the contour
    # The x-coordinate of the center is given by the ratio of the "m10" moment to the "m00" moment
    c_x = int(M["m10"] / M["m00"])

    # Calculate the y-coordinate of the center of the contour
    # The y-coordinate of the center is given by the ratio of the "m01" moment to the "m00" moment
    c_y = int(M["m01"] / M["m00"])

    # Draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (255, 255, 255), 2)
    cv2.circle(image, (c_x, c_y), 7, (255, 255, 255), -1)

    # Add text "center" near the center of the shape
    cv2.putText(image, "center", (c_x - 20, c_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
```

Explanation:

1. The `cv2.moments(c)` function computes a set of moments for the current contour `c`.
Moments are statistical measures that describe the shape and spatial distribution of the contour.

2. `M["m10"]` represents the first-order moment in the x-direction, and `M["m01"]`
represents the first-order moment in the y-direction. These moments describe the spatial
 distribution of mass in the contour.

3. `M["m00"]` represents the zeroth-order moment, which is the total mass or area of the contour.
It is used to normalize the moments to calculate the center coordinates.

4. `C_x` is calculated by dividing the first-order moment in the x-direction (`M["m10"]`)
 by the zeroth-order moment (`M["m00"]`). This gives the x-coordinate of the center of the contour.

5. `C_y` is calculated similarly by dividing the first-order moment in the y-direction (`M["m01"]`)
by the zeroth-order moment (`M["m00"]`). This gives the y-coordinate of the center of the contour.

6. After calculating the center coordinates (`c_x` and `c_y`), the code draws the contour,
places a circle at the center, and adds the text "center" near the center of the shape on the image for visualization.

These calculations and visualizations help in understanding the position of the center of each
detected contour in the image.
Epsilon is a parameter used for contour approximation. It controls how closely the approximation
matches the original contour. In this code, epsilon is calculated as a small fraction (0.001) of
the contour's arc length using cv2.arcLength(c, True).

cv2.approxPolyDP(c, epsilon, True) is used to approximate the original contour c with fewer
vertices while ensuring that it remains a closed contour (True argument). The resulting data
contains the vertices of the approximated contour.

The cv2.convexHull(data) function is used to calculate the convex hull of the approximated contour.
The convex hull is the smallest convex shape that encloses all the vertices of the approximated contour.

The x, y, w, and h values are calculated using cv2.boundingRect(hull), which computes the bounding
rectangle around the convex hull. These values represent the position (top-left corner) and dimensions
(width and height) of the bounding rectangle.

Finally, cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 5) draws a white rectangle
around the convex hull on the original image. The (255, 255, 255) argument specifies the color (white),
and 5 specifies the thickness of the rectangle's border."""

# Import the OpenCV library
import cv2

# Load an image and get its dimensions
image = cv2.imread("images/1200px-OpenCV_Logo_with_text_svg_version.svg.png")
height, width = image.shape[:2]
area_1 = []

# Calculate the aspect ratio to maintain proportions when resizing
ratio = float(width) / float(height)

# Ask the user to input the new height for the image
new_height = int(input("Enter the new height: "))

# Calculate the new width using the aspect ratio
new_width = int(ratio * new_height)

# Resize the image to the new dimensions
image = cv2.resize(image, (new_width, new_height))

# Create a grayscale version of the resized image
image_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a binary threshold to the grayscale image
ret, thresh = cv2.threshold(image_1, 50, 255, cv2.THRESH_BINARY)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Print the contours and their count
print("Contours:", contours)
print("Number of Contours:", len(contours))
print("Hierarchy:", hierarchy)

# Draw the contours on the original image
image = cv2.drawContours(image, contours, -1, (255, 255, 255), 5)

# Loop over the contours
for c in contours:
    # Compute the center of the contour using image moments
    M = cv2.moments(c)
    c_x = int(M["m10"] / M["m00"])
    c_y = int(M["m01"] / M["m00"])

    # Draw the contour and center of the shape on the image
    cv2.drawContours(image, [c], -1, (255, 255, 255), 2)
    cv2.circle(image, (c_x, c_y), 7, (255, 255, 255), -1)
    # Find are of Contour
    area = cv2.contourArea(c)
    area_1.append(area)

    '''The code below is used to calculate the least number of vertices that can be used to enclose the figure'''
    # Contour approx - it is used to approx shape with less numb of vertices
    # Calculate the epsilon value for contour approximation
    epsilon = 0.001 * cv2.arcLength(c, True)

    # Approximate the contour with fewer vertices using the calculated epsilon value
    data = cv2.approxPolyDP(c, epsilon, True)

    # The 'epsilon' value controls how closely the approximation matches the original contour.
    # Smaller 'epsilon' values result in a closer approximation, while larger values produce a more simplified contour.
    # The 'True' argument indicates that the contour is closed (the last and first points are connected).

    # Print the approximated contour data (vertices)
    print(data)

    # Convex hull is used to provide the convexity of the contours
    hull = cv2.convexHull(data)

    # Calculate the bounding rectangle around the convex hull
    x, y, w, h = cv2.boundingRect(hull)

    # Draw a rectangle around the convex hull on the image
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 5)

    # Add text "center" near the center of the shape
    cv2.putText(image, "center", (c_x - 20, c_y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

# Display the original image and the thresholded image
cv2.imshow("Original", image)
cv2.imshow("Threshold", thresh)

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
