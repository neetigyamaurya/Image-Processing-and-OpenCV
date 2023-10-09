"""Contours
can be explained simply as a curve joining all the continuous points(along the boundary), having the same color
or intensity.
The contours are a useful tool for shape analysis and object detection
For better accuracy use binary images and also apply edge detection before finding contours

findContour function manipulates the original image so copy it before proceeding.
findContour is like finding white objects
black background. You must turn the image in white and background in black.
We have to find and draw contours as per the requirements
"""
import cv2

image = cv2.imread('images/1200px-OpenCV_Logo_with_text_svg_version.svg.png')
height, width = image.shape[:2]
ratio = float(width) / float(height)
new_height = int(input("Enter new height: "))
new_width = int(new_height * ratio)
image = cv2.resize(image, (new_width, new_height))
image_1 = image
image_1 = cv2.cvtColor(image_1, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(image_1, 25, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours, len(contours))
# Now we draw these contours
image = cv2.drawContours(image, contours, -1, (255, 255, 255), 4)  # -1 ki wajh se saare contours
# detect ho jaynge
cv2.imshow('Original', image)
cv2.imshow('Threshold', thresh)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
