# Python program to illustrate
# Background subtraction using
# the concept of Running Averages
"""The objective of the program is to detect active objects from the difference obtained from the reference
frame and the current frame. We keep feeding each frame to the given function, and the function keeps finding
the averages of all frames. Then we compute the absolute difference between the frames.
---------------------------------cv2.accumulateWeighted(src, dst, alpha)------------------------------------------------

src: The source image. The image can be colored or grayscale image and either 8-bit or 32-bit floating point.
dst: The accumulator or the destination image. It is either 32-bit or 64-bit floating point.
NOTE: It should have the same channels as that of the source image. Also, the value of dst should be predeclared
initially.
alpha: Weight of the input image. Alpha decides the speed of updating. If you set a lower value for this variable,
running average will be performed over a larger number of previous frames and vice-versa."""

# organize imports
import cv2
import numpy as np


def resize(image, new_height):
    # Figure out how wide the picture should be to keep it looking nice
    h, w = image.shape[:2]  # This tells us the picture's height and width
    ratio = float(w) / float(h)  # Imagine the picture's width compared to its height
    new_width = int(ratio * new_height)  # This is how wide the picture should be
    resized_image = cv2.resize(image, (new_width, new_height))  # Make the picture the right size
    return resized_image  # Get the new, smaller picture


# capture frames from a video file
cap = cv2.VideoCapture('images/traffic.mp4')

# read the frames from the file
_, img = cap.read()
img = resize(img, 900)

# modify the data type
# setting to 32-bit floating point
averageValue1 = np.float32(img)
print(averageValue1)
# loop runs if capturing has been initialized.
while cap.isOpened():
    # reads frames from a camera
    ret, img = cap.read()
    if not ret:
        print("Error opening video stream or file")
        break
    img = resize(img, 900)
    # using the cv2.accumulateWeighted() function
    # that updates the running average
    test = cv2.accumulateWeighted(img, averageValue1, 0.002)

    # converting the matrix elements to absolute values
    # and converting the result to 8-bit.
    resultingFrames1 = cv2.convertScaleAbs(test)

    # Show two output windows
    # the input / original frames window
    cv2.imshow('InputWindow', img)
    # cv2.imshow('OutputWindow', averageValue1)
    # the window showing output of alpha value 0.002
    cv2.imshow('Result', resultingFrames1)

    # Wait for q to stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
