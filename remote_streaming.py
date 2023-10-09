import cv2
'''
camera_address = "http://192.168.1.36:8080/video"
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("Phone_Camera-2.avi", fourcc, 24, (1280, 720))

cap = cv2.VideoCapture(0)
cap.open(camera_address)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        #frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        #frame = cv2.flip(frame, 1)
        cv2.imshow(f"{camera_address}", frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            output.release()
            cap.release()
            cv2.destroyAllWindows()
        if k == ord("s"):
            output.write(frame)
        else:
            continue
'''


camera_address = "http://192.168.1.36:8080/video"
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("Phone_Camera-2.avi", fourcc, 24, (1280, 720))

cap = cv2.VideoCapture(camera_address)  # Open the IP camera

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        cv2.imshow(f"{camera_address}", frame)
        k = cv2.waitKey(1)
        if k == ord("q"):
            output.release()
            cap.release()
            cv2.destroyAllWindows()
        if k == ord("s"):
            output.write(frame)
    else:
        break
