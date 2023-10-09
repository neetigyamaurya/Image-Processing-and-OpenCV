# Bitwise operations on Images

import cv2
import numpy as np

img_1 = np.zeros((250, 500, 3), np.uint8)
img_1 = cv2.rectangle(img_1, (150, 100), (200, 250), (255, 255, 255), -1)
img_2 = np.zeros((250, 500, 3), np.uint8)
img_2 = cv2.rectangle(img_2, (10, 10), (170, 190), (255, 255, 255), -1)
bitwise = cv2.bitwise_and(img_1, img_2)
bitwise_or = cv2.bitwise_or(img_1, img_2)
bitwise_not = cv2.bitwise_not(img_1)
bitwise_xor = cv2.bitwise_xor(img_1, img_2)
cv2.imshow("Test_2", img_2)
cv2.imshow("Test", img_1)
cv2.imshow("Bitwise-AND", bitwise)
cv2.imshow("BitwiseOR", bitwise_or)
cv2.imshow("BitwiseNot", bitwise_not)
cv2.imshow("BitwiseXOR", bitwise_xor)
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
