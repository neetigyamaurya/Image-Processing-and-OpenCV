# We use image pyramid because sometimes we work on the same image but different resolution e.g., searching
# face, eye in an
# image and caries image to image, so in this case we create a set of
# images with different resolution which is called# pyramid.
# We also use these pyramids to blend images

# There are two types of image pyramid 1) Gaussian Pyramid 2) Laplacian Pyramids

import cv2

image = cv2.imread('images/ColorWall-lqwzor.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

height, width = image.shape[:2]
ratio = float(width) / float(height)
new_height = int(input("Enter the new height : "))
new_width = int(ratio * new_height)
image = cv2.resize(image, (new_width, new_height))
# Gaussian Pyramid have two functions 1) PyrUp 2) pyrDown
pd_1 = cv2.pyrDown(image)
pup_1 = cv2.pyrUp(image)

cv2.imshow('image', image)
cv2.imshow('Pyramid', pd_1)
cv2.imshow("Up", pup_1)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
