import cv2

cap = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow('Webcam-0')
cv2.createTrackbar("Thresh Binary Lower", "Webcam-0", 50, 255, nothing)
cv2.createTrackbar("Thresh Binary Upper", "Webcam-0", 255, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if frame.size > 0:
            lower = cv2.getTrackbarPos("Thresh Binary Lower", "Webcam-0")
            upper = cv2.getTrackbarPos("Thresh Binary Upper", "Webcam-0")
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _, th_1 = cv2.threshold(frame, lower, upper, cv2.THRESH_BINARY)
            print("----------------------------Running-----------------------------------")
            print(lower)
            print(upper)
            if cv2.waitKey(24) == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break
        else:
            pass
    else:
        pass
