import cv2
import numpy as np


def mouse_event(event, x, y, flags, params):
    """
    Handle mouse events.

    Parameters:
    - event: The type of mouse event.
    - x: The x-coordinate of the mouse cursor.
    - y: The y-coordinate of the mouse cursor.
    - flags: Additional flags for the event.
    - params: Additional parameters (not used in this function).

    This function prints information about the mouse event and displays text on the image
    when left or right mouse buttons are double-clicked.

    For left mouse button double-click:
    - Displays the coordinates (x, y) at the clicked position on the image.

    For right mouse button double-click:
    - Extracts the BGR color values at the clicked position and displays them on the image.

    Returns:
    None
    """
    print("Event:", event)
    print("X : ", x)
    print("Y : ", y)
    print("Params:", params)
    font = cv2.FONT_HERSHEY_COMPLEX

    # Handle left mouse button double-click
    if event == cv2.EVENT_LBUTTONDOWN:
        cord = str(x) + " " + str(y)
        cv2.putText(img, cord, (x, y), font, 1, (155, 154, 180), 2, cv2.LINE_AA)

    # Handle right mouse button double-click
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]  # Extract blue channel value at the clicked position
        g = img[y, x, 1]  # Extract green channel value at the clicked position
        r = img[y, x, 2]  # Extract red channel value at the clicked position
        color_bgr = str(b) + " " + str(g) + " " + str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (155, 154, 180), 2, cv2.LINE_AA)


# Create a named window for displaying shapes
cv2.namedWindow(winname="SHAPES")

# Create a black image with dimensions 1000x1000 and 3 color channels
img = np.zeros((1000, 1000, 3), dtype=np.uint8)
# Set a mouse callback function for the "SHAPES" window
cv2.setMouseCallback("SHAPES", mouse_event)

while True:
    # Display the image in the "SHAPES" window
    cv2.imshow("SHAPES", img)

    # Wait for a key press (1 millisecond) and check if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
