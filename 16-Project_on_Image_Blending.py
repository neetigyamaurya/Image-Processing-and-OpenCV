import cv2
import numpy as np

black = cv2.imread("Black.png")
white = cv2.imread("White.png")

blank = np.zeros((500, 500, 3))


def blend(x):
    pass


cv2.namedWindow("Merged")
cv2.createTrackbar("Alpha", "Merged", 1, 100, blend)
switch = "0:OFF" + "\n" + "1:ON"
cv2.createTrackbar(switch, "Merged", 0, 1, blend)
while True:
    s = cv2.getTrackbarPos(switch, "Merged")
    a = cv2.getTrackbarPos("Alpha", "Merged")
    a = float(a / 100)
    if s == 0:
        dst = blank[:]
    else:
        dst = cv2.addWeighted(black, a, white, 1 - a, 0)
    cv2.imshow("Merged", dst)
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
