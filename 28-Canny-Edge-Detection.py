# Canny-Edge Detection is one of the most powerful techniques
# It uses multi-stage algorithm to detect an edges
# This approach combines 5 steps=
# Noise reduction (gauss)  ----> Gradient Calculation ----> Non Maximum Suppression ---->
# Double Threshold ----> Edge Tracking by Hysteresis

import cv2


def nothing(x):
    pass


image = cv2.imread('images/ColorWall-lqwzor.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

old_height, old_width = image.shape[:2]  # image.shape ---------> height,width
ratio = float(old_width) / float(old_height)
new_height = int(input("Enter the new height: "))
new_width = int(new_height * ratio)
image = cv2.resize(image, (new_width, new_height))
cv2.namedWindow("Canny Edge Detection")
cv2.createTrackbar("Threshold", "Canny Edge Detection", 0, 255, nothing)

while True:
    position = cv2.getTrackbarPos("Threshold", "Canny Edge Detection")
    canny_edge = cv2.Canny(image, position, 255)
    cv2.imshow("Canny Edge Detection", canny_edge)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
