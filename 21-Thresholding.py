# Thresholding
#  is the binarization of an image. In general, we seek to convert a grayscale image to a binary image,
# where the pixels are either 0 or 255.
# A simple thresholding example would be selecting a threshold value t, and then setting all pixel intensities less
# than t to 0, and all pixel values greater than t to 255. In this way, we are able to create a binary
# representation of the image.
# Thresholding is a popular segmentation technique used for separating an object from its background.
# Thresholding is also used for feature extraction, where our goal is to take some measurement or combination of
# measurements from an image that are relevant to the ability of humans to interpret the contents of that image.
# Thresholding is also used for image processing applications such as denoising and contrast enhancement.
# Thresholding is also used for document processing applications such as OCR.
# simple thresholding(img,pixel_thresh, max_thresh_pixel,style)
import cv2

img = cv2.imread("images/Gradient-of-low-contrast-650x433.jpg", 0)
cv2.imshow("Gradient-of-low", img)
temp, th_1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
temp, th_2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)
_, th_3 = cv2.threshold(img, 50, 255, cv2.THRESH_TRUNC)
_, th_4 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO)
_, th_5 = cv2.threshold(img, 50, 255, cv2.THRESH_TOZERO_INV)
cv2.imshow("Binary Thresholding", th_1)
cv2.imshow("Binary Thresholding Inverse", th_2)
cv2.imshow("Truncated Binary Thresholding", th_3)
cv2.imshow("Thresh to Zero", th_4)
cv2.imshow("Thresh to Zero Inverse", th_5)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
