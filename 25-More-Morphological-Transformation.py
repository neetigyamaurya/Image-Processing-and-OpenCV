# Opening and closing are 2 more morphological operations
# 1-Opening,2-Closing
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("2704.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.resize(image, (500, 500))
hold = image
_, mask = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY_INV)
kernel_err = np.ones((3, 3), np.uint8)
erosion = cv2.erode(mask, kernel_err)
kernel_dil = np.ones((2, 2), np.uint8)
dilation = cv2.dilate(mask, kernel_dil)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_dil)
kernel_closing = np.ones((3, 3), np.uint8)
# In closing dilation is performed before erosion
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_closing)
# -----------------------------------------------OPTIONAL----------------------------------------------------------------
x_1 = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernel_closing)  # It is the difference between mask and opening
x_2 = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel_closing)  # Difference between dilation and erosion
x_3 = cv2.morphologyEx(mask, cv2.MORPH_BLACKHAT, kernel_closing)
cv2.imshow("Original", image)
cv2.imshow("Mask", mask)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Tophat", x_1)
cv2.imshow("Morphological Gradient", x_2)
cv2.imshow("Morphological Blackhat", x_3)
titles = ['Original', 'Mask', 'Erosion', 'Dilation', 'Opening', 'Closing', 'Tophat', 'Morphological Gradient',
          'Morphological Blackhat']
images = [image, mask, erosion, dilation, opening, closing, x_1, x_3, x_3]
for i in range(9):
    plt.subplot(3, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
fig = plt.gcf()
fig.set_size_inches(20, 20)
plt.show()

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
