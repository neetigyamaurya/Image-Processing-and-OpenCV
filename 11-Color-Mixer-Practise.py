import cv2
import numpy


def cross(x):
    pass


img = numpy.zeros((400, 800, 3), dtype=numpy.uint8)

cv2.namedWindow("Color-Mixer")

s_1 = f"0->OFF\n1->ON"

cv2.createTrackbar(s_1, "Color-Mixer", 0, 1, cross)
cv2.createTrackbar("B", "Color-Mixer", 0, 255, cross)
cv2.createTrackbar("G", "Color-Mixer", 0, 255, cross)
cv2.createTrackbar("R", "Color-Mixer", 0, 255, cross)


while True:
    cv2.imshow("Color-Mixer", img)
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break
    s = cv2.getTrackbarPos(s_1, "Color-Mixer")
    b = cv2.getTrackbarPos("B", "Color-Mixer")
    g = cv2.getTrackbarPos("G", "Color-Mixer")
    r = cv2.getTrackbarPos("R", "Color-Mixer")
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv2.destroyAllWindows()
