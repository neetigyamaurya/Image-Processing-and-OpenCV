import cv2
import numpy as np


# Define a callback function for the trackbars (not used in this example)
def cross(x):
    pass


# Create a black blank image
img = np.zeros((600, 400, 3),
               dtype=np.uint8)

# Create a named window for the color mixer
cv2.namedWindow("Color Mixer")

# Create an on-off switch using a trackbar
s_1 = "0:OFF\n1:ON"
cv2.createTrackbar(s_1, "Color Mixer", 0, 1, cross)

# Create trackbars for adjusting BGR color components
cv2.createTrackbar("B", "Color Mixer", 0, 255, cross)
cv2.createTrackbar("G", "Color Mixer", 0, 255, cross)
cv2.createTrackbar("R", "Color Mixer", 0, 255, cross)

while True:
    # Display the color mixer window
    cv2.imshow("Color Mixer", img)

    # Check for a key press ('q') to exit
    if cv2.waitKey(1) == ord("q"):
        cv2.destroyAllWindows()
        break

    # Get the position of the on-off switch trackbar
    s = cv2.getTrackbarPos(s_1, "Color Mixer")

    # Get the positions of the BGR color trackbars
    b = cv2.getTrackbarPos("B", "Color Mixer")
    g = cv2.getTrackbarPos("G", "Color Mixer")
    r = cv2.getTrackbarPos("R", "Color Mixer")

    # Update the image based on the trackbar positions
    if s == 0:
        img[:] = 0  # Turn off color if the switch is off
    else:
        img[:] = [b, g, r]  # Set the color to the selected BGR values

# Close all OpenCV windows
cv2.destroyAllWindows()
