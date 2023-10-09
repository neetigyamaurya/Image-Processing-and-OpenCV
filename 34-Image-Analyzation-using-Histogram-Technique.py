# Image Histogram - Find, Plot and Analyze
# It which gives you an overall idea about the intensity distribution of an image
# It distributes data along x and y-axis
# x-axis contains range of color values
# y-axis contains numbers of pixels in an image
# Plot histogram to extract information about contrast,brightness and intensity.


import cv2
import matplotlib.pyplot as plt

# image = np.zeros((200, 200), np.uint8)
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
b, g, r = cv2.split(image)
# cv2.rectangle(image, (0, 100), (200, 200), 255, -1)
# cv2.rectangle(image, (0, 50), (50, 100), 127, -1)

histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.hist(b.ravel(), 256, (0, 256))
plt.hist(g.ravel(), 256, (0, 256))
plt.hist(r.ravel(), 256, (0, 256))
plt.title("Histogram")
plt.plot(histogram)
plt.show()
cv2.imshow("Image", image)
cv2.imshow("Blur", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
