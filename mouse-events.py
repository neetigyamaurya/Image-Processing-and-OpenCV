import cv2
import numpy


# Define a function 'draw' to handle mouse events
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("X---> ", x)
        print("Y---> ", y)
        print("Param----> ", param)
        # Draw a circle at the double-clicked position with a radius of 100 and color (180, 72, 97)
        cv2.circle(img, (x, y), 100, (180, 72, 97), 1)
    if event == cv2.EVENT_RBUTTONDBLCLK:
        # Draw a rectangle at the double-clicked position with a size of (100, 800) and color (220, 58, 150)
        cv2.rectangle(img, (x, y), (x + 100, y + 800), (220, 58, 150), 2)


# Create a named window for displaying shapes
cv2.namedWindow(winname="SHAPES")

# Create a black image with dimensions 1000x1000 and 3 color channels
img = numpy.zeros((1000, 1000, 3), dtype=numpy.uint8)

# Set a mouse callback function for the "SHAPES" window
cv2.setMouseCallback("SHAPES", draw)

while True:
    # Display the image in the "SHAPES" window
    cv2.imshow("SHAPES", img)

    # Wait for a key press (1 millisecond) and check if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
