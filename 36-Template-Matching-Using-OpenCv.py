"""
Template Matching

This code demonstrates template matching, a method used to search for and locate a template image within a larger image.
OpenCV provides the function cv2.matchTemplate() for this purpose. The function slides the template image over the input
image, comparing the template and a patch of the input image at each position.

The code performs the following steps:
1. Loads the target image and the template image.
2. Converts both images to grayscale for template matching.
3. Applies template matching using cv2.matchTemplate().
4. Sets a threshold to find matching regions.
5. Draws rectangles around the matching regions in the target image
It is a method of searching and finding the location of a template images in a larger image. OpenCv comes with a
function cv2.matchTemplate() for this purpose. It simply slides the template image over the input image (as in
2-D convolution) and compares the template and patch of input image."""
import cv2
import numpy as np

# Target Image
image = cv2.imread('images/bg-sep.jpg')
image_in_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Template Image
template = cv2.imread('images/head.jpg')
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
height, width = template.shape[:2]  # img.shape returns (Height, Width, Number of Channels)

# Template matching ---> This function accepts parameter (img,template, method)
res = cv2.matchTemplate(image_in_grayscale, template, cv2.TM_CCOEFF_NORMED)


def resize(image, new_height):
    """This function returns the resized image while preserving the aspect ratio."""
    h, w = image.shape[:2]
    ratio = float(w) / float(h)
    new_width = int(ratio * new_height)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image


threshold = 0.95
loc = np.where(res >= threshold)  # Finding the brightest pixel # Will store as width ,height
for count, i in enumerate(zip(*loc[
                               ::-1])):  # *: The asterisk * is the unpacking operator in Python.
    # It is used to unpack the values from an iterable (in this case, a tuple of arrays) into separate
    # arguments for a function or into a list.
    '''
    In OpenCV's `cv2.matchTemplate` function and related functions, the output of `np.where` 
    and the coordinates used to specify rectangles in OpenCV functions are typically specified as `(x, y)` 
    where `x` represents the horizontal position (width) and `y` represents the vertical position (height).
    So, in the context of `cv2.matchTemplate` and related functions, 
    the coordinates are `(x, y)` where `x` is the width (horizontal) and `y` 
    is the height (vertical).
    '''
    print("i==", i)
    # cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
    cv2.rectangle(image, i, (i[0] + width, i[1] + height), (0, 0, 255), 2)

new_height = int(input("Enter the new Height of the image: "))
image = resize(image, new_height)
cv2.imshow('Image', image)
height, width = image.shape[:2]
res = cv2.resize(res, (width, height))
cv2.imshow('Template', res)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
