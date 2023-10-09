# 1) Extract different channels from a video and store them separately.
import cv2

count = 0
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        if frame is not None and frame.size != 0:
            count += 1
            frame = cv2.flip(frame, 1)
            b, g, r = cv2.split(frame)
            cv2.imshow("Player", frame)
            cv2.imwrite(f"/home/neetigya-maurya/Videos/b/blue{count}.jpg", b)
            cv2.imshow("Blue", b)
            cv2.imshow("Green", g)
            cv2.imwrite(f"/home/neetigya-maurya/Videos/g/green{count}.jpg", g)
            cv2.imshow("Red", r)
            cv2.imwrite(f"/home/neetigya-maurya/Videos/r/red{count}.jpg", r)
            print(f"Frame Num: {cap.get(cv2.CAP_PROP_POS_FRAMES)}")
            if cv2.waitKey(24) == ord("q"):
                cap.release()
                cv2.destroyAllWindows()
                break
