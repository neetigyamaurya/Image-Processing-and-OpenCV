import cv2
import numpy


def do_nothing(x):
    pass


# Create a named Window
cv2.namedWindow("Player")

# Creating Trackbar
cv2.createTrackbar("Lower Hue Range", "Player", 0, 255, do_nothing)
cv2.createTrackbar("Lower Saturation Range", "Player", 0, 255, do_nothing)
cv2.createTrackbar("Lower Value Range", "Player", 0, 255, do_nothing)

cv2.createTrackbar("Upper Hue Range", "Player", 255, 255, do_nothing)
cv2.createTrackbar("Upper Saturation Range", "Player", 255, 255, do_nothing)
cv2.createTrackbar("Upper Value Range", "Player", 255, 255, do_nothing)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frames = cap.read()
    if ret:
        hsv = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)
        lower_hue_range = cv2.getTrackbarPos("Lower Hue Range", "Player")
        lower_saturation_range = cv2.getTrackbarPos("Lower Saturation Range", "Player")
        lower_value_range = cv2.getTrackbarPos("Lower Value Range", "Player")
        upper_hue_range = cv2.getTrackbarPos("Upper Hue Range", "Player")
        upper_saturation_range = cv2.getTrackbarPos("Upper Saturation Range", "Player")
        upper_value_range = cv2.getTrackbarPos("Upper Value Range", "Player")
        ###################################DEBUGING CODE CAN BE REMOVED####################################
        # print("Lower Hue:", lower_hue_range)
        # print("Upper Hue:", upper_hue_range)
        # print("Lower Saturation:", lower_saturation_range)
        # print("Upper Saturation:", upper_saturation_range)
        # print("Lower Value:", lower_value_range)
        # print("Upper Value:", upper_value_range)
        # --------------------------------------------------------------------------------------------------#
        lower_limit = numpy.array(
            [lower_hue_range, lower_saturation_range, lower_value_range]
        )
        upper_limit = numpy.array(
            [upper_hue_range, upper_saturation_range, upper_value_range]
        )
        cv2.imshow("Player", frames)
        # Creating Mask
        live_mask = cv2.inRange(hsv, lower_limit, upper_limit)
        cv2.imshow("Mask", live_mask)
        result = cv2.bitwise_and(frames, frames, mask=live_mask)
        cv2.imshow("Result", result)
        if cv2.waitKey(1) == ord("q"):
            cap.release()
            break
cv2.destroyAllWindows()
