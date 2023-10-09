import cv2

img = cv2.imread("images/ilona-bellotto-rbPplWrpgcU-unsplash.jpg", 0)
img = cv2.resize(img, (640, 480))
th_1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
_, th_2 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
th_3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow("img", img)
cv2.imshow("Thresholding", th_1)
cv2.imshow("Simple Thresholding", th_2)
cv2.imshow("Gaussian Thresholding", th_3)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
