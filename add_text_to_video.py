import datetime

import cv2

PATH = "1.webm"
FONT = cv2.FONT_HERSHEY_COMPLEX
DATE = str(datetime.datetime.now())
cap = cv2.VideoCapture(PATH)
ret, frames = cap.read()
print(f"Frame Width: {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
print(f"Frame Height: {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
print(f"Frame Width: {cap.get(3)}")
print(f"Frame Height: {cap.get(4)}")
while cap.isOpened():
    ret, frames = cap.read()
    if ret:
        if frames is not None and frames.size != 0:
            text = "Height: " + str(cap.get(4)) + " Width:  " + str(cap.get(3))
            cv2.putText(frames, text, (10, 20), FONT, 1, (0, 155, 155), 2, cv2.LINE_AA)
            cv2.putText(
                frames,
                str(cap.get(cv2.CAP_PROP_POS_FRAMES)),
                (40, 50),
                FONT,
                1,
                (0, 155, 155),
                1,
                cv2.LINE_AA,
            )
            cv2.putText(frames, DATE, (70, 90), FONT, 1, (0, 155, 155), 2, cv2.LINE_AA)
            cv2.imshow(f"{PATH}", frames)
            if cv2.waitKey(24) == ord("q"):
                cap.release()
                cv2.destroyAllWindows()
            else:
                continue
        else:
            continue
    else:
        print("Frames were not found")
        break
