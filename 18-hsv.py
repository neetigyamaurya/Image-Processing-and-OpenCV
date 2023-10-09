import cv2
import numpy


def color_picker(event, x, y, flags, param):
    """This will receive the mouse event and return the color of the pixel clicked"""
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        text = f"({b},{g},{r})"
        cv2.putText(img, text, (x, y), font, 1, (255, 255, 255), 4, cv2.LINE_AA)
        print(text)


cv2.namedWindow("Image")
img = cv2.imread("/home/neetigya-maurya/Downloads/balls.jpg", 1)
while True:
    cv2.setMouseCallback("Image", color_picker)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_limit = numpy.array([16, 120, 72])
    upper_limit = numpy.array([60, 250, 87])
    mask = cv2.inRange(hsv, lower_limit, upper_limit)
    filter = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filter", filter)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
