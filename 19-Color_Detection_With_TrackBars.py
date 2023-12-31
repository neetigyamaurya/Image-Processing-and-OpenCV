import cv2
import numpy

img_1 = cv2.imread("images//balls.jpg", 1)


def resize(image, new_height):
    # Figure out how wide the picture should be to keep it looking nice
    h, w = image.shape[:2]  # This tells us the picture's height and width
    ratio = float(w) / float(h)  # Imagine the picture's width compared to its height
    new_width = int(ratio * new_height)  # This is how wide the picture should be
    resized_image = cv2.resize(image, (new_width, new_height))  # Make the picture the right size
    return resized_image  # Get the new, smaller picture


img_1 = resize(img_1, 500)


def nothing(x):
    pass


cv2.namedWindow("Color Detection")
cv2.createTrackbar("Lower Hue Range", "Color Detection", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation Range", "Color Detection", 0, 255, nothing)
cv2.createTrackbar("Lower Value Range", "Color Detection", 0, 255, nothing)

cv2.createTrackbar("Upper Hue Range", "Color Detection", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation Range", "Color Detection", 255, 255, nothing)
cv2.createTrackbar("Upper Value Range", "Color Detection", 255, 255, nothing)

while True:
    hsv = cv2.cvtColor(img_1, cv2.COLOR_BGR2HSV)
    l_hue = cv2.getTrackbarPos("Lower Hue Range", "Color Detection")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color Detection")
    l_value = cv2.getTrackbarPos("Lower Value Range", "Color Detection")

    u_hue = cv2.getTrackbarPos("Upper Hue Range", "Color Detection")
    u_s = cv2.getTrackbarPos("Upper Saturation Range", "Color Detection")
    u_v = cv2.getTrackbarPos("Upper Value Range", "Color Detection")

    lower_bound = numpy.array([l_hue, l_saturation, l_value])
    upper_bound = numpy.array([u_hue, u_s, u_v])
    # Creating Mask
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(img_1, img_1, mask=mask)

    cv2.imshow("Color Detection", img_1)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)
    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
