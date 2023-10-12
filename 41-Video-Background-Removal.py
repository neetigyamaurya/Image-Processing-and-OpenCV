"""Background Subtraction is a way to access the foreground objects. You need to extract the moving foreground objects
from the static background image. """
import cv2


def resize(image, new_height):
    # Figure out how wide the picture should be to keep it looking nice
    h, w = image.shape[:2]  # This tells us the picture's height and width
    ratio = float(w) / float(h)  # Imagine the picture's width compared to its height
    new_width = int(ratio * new_height)  # This is how wide the picture should be
    resized_image = cv2.resize(image, (new_width, new_height))  # Make the picture the right size
    return resized_image  # Get the new, smaller picture


algo_1 = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
algo_2 = cv2.createBackgroundSubtractorKNN(detectShadows=True)  # This works better

cap = cv2.VideoCapture('images/traffic.mp4')
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        frame = resize(frame, 400)
        res_1 = algo_1.apply(frame)
        res_2 = algo_2.apply(frame)
        cv2.imshow('Traffic', frame)
        cv2.imshow('Algo 1', res_1)
        cv2.imshow('Algo 2', res_2)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
