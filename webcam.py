import sys

import cv2

cap = cv2.VideoCapture(0)  # 0 for webcam
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter(
    "output.avi",
    fourcc,
    24,
    (640, 480),  # ADD 0 if you want the video to be saved as gray scale
)  # Name,Codec,FPS,Resolution


while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(f"Frame Num: {cap.get(cv2.CAP_PROP_POS_FRAMES)}")  # Frame Number
        frame = cv2.flip(frame, 1)
        cv2.imshow("Webcam", frame)
        output.write(frame)
        print(sys.getrefcount(frame))
        k = cv2.waitKey(24)
        if k == ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            output.release()
            break
        if k == ord("s"):
            output.write(frame)
        else:
            continue
