# Circle detection using Hough Circle and OpenCV

import cv2
import numpy as np

'''
def resize(image, new_height):
    """This function returns the resized image while preserving the aspect ratio."""
    h, w = image.shape[:2]
    ratio = float(w) / float(h)
    new_width = int(ratio * new_height)
    resized_image = cv2.resize(image, (new_width, new_height))
    return resized_image


image = cv2.imread('images/balls.jpg')
new_height = int(input("Enter the new height of the image: "))
image = resize(image, new_height)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
_, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# parameters ---->(img,circle_method,dp,mindist,param1,param2[p1>p2],minradius,maxradius)
circles = cv2.HoughCircles(opening,
                           cv2.HOUGH_GRADIENT,
                           1,
                           100,
                           param1=70,
                           param2=40,
                           minRadius=20,
                           maxRadius=0)
# param 1 and param 2 can be
# thought of as the distance between two pixels
# Even if minimum radius is 0 it is fine and the max radius is 0 is fine. No limit specified
print(circles)  # circles will give output as float so we need to convert it to integer.
data = np.uint16(np.around(circles))
print(data)

for (x, y, r) in data[0, :]:
    cv2.circle(image, (x, y), r, (52, 53, 97), 3)  # Outer circle
    cv2.circle(image, (x, y), 2, (34, 255, 18), -1)  # Center

cv2.imshow('image', image)
# cv2.imshow('gray', gray)
# cv2.imshow('thresh', thresh)
# cv2.imshow('Opening', opening)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
'''
# -----------------------------------------Using Webcam-----------------------------------------------------------------
cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
while cap.isOpened():
    ret, frame = cap.read()
    print(ret)
    if not ret:
        print("Error opening video stream or file")
        break
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)  # This increases the computational
    # complexity, remove this if your window is stuttering, not opening.
    blur = cv2.medianBlur(thresh, 5)
    opening = cv2.morphologyEx(blur, cv2.MORPH_OPEN, kernel)
    circles = cv2.HoughCircles(opening,
                               cv2.HOUGH_GRADIENT,
                               1,
                               100,
                               param1=70,
                               param2=40,
                               minRadius=20,
                               maxRadius=0)
    if circles is not None:
        data = np.uint16(np.around(circles))
        for (x, y, r) in data[0, :]:
            cv2.circle(frame, (x, y), r, (50, 10, 50), 3)  # Outer circle
            cv2.circle(frame, (x, y), 2, (0, 255, 100), -1)  # Inner Circle
            print("Done")
        cv2.imshow('Display', frame)
        if cv2.waitKey(12) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
cv2.destroyAllWindows()
