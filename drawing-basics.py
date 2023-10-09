import cv2
import numpy as np  # Import numpy as np for better readability

# Create a black image with dimensions 1000x1000 and three color channels
img = np.zeros([1000, 1000, 3], dtype=np.uint8)*255  # Use np.uint8 for an image data type

# Draw lines on the image
img = cv2.line(
    img, (0, 0), (200, 200), (154, 92, 42), 8
)  # Draw a line from (0,0) to (200,200) with color (BGR) (154, 92, 42) and thickness 8
img = cv2.line(img, (200, 200), (800, 200), (154, 92, 42), 8)  # Draw another line
img = cv2.line(img, (800, 200), (1000, 1000), (154, 92, 42), 8)  # Draw another line yet

# Draw a filled rectangle on the image
img = cv2.rectangle(
    img, (0, 0), (500, 500), (100, 150, 20), -1
)  # Filled rectangle from (0,0) to (500,500) with color (BGR) (100, 150, 20)

# Draw an arrowed line
img = cv2.arrowedLine(
    img, (500, 500), (800, 800), (189, 129, 39), 8
)  # Arrowed line from (500,500) to (800,800) with color (BGR) (189, 129, 39)

# Draw a filled circle
img = cv2.circle(
    img, (800, 800), 190, (154, 92, 25), -1
)  # Filled circle with center (800,800), radius 190, and color (BGR) (154, 92, 25)

# Add text to the image
img = cv2.putText(
    img,
    "NEETIGYA",
    (900, 900),
    cv2.FONT_HERSHEY_COMPLEX,
    4,
    (154, 92, 42),
    10,
    cv2.LINE_AA,
)
# Put the text "NEETIGYA" at position (900, 900)
# with font size 4, color (BGR) (154, 92, 42),
# thickness 10, and using anti-aliased lines

# Draw an ellipse
img = cv2.ellipse(
    img, (400, 600), (100, 50), 0, 0, 270, (155, 5)
)  # Draw an ellipse with center (400,600), axes (100,50), angle 0, startAngle 0, endAngle 270, and color (BGR) (155, 5)

# Display the image in a window
cv2.imshow("COMPARE_BW", img)

# Wait for a key press and check if it's the 'q' key
k = cv2.waitKey(0)

# If 'q' is pressed, close the image window
if k == ord("q"):
    cv2.destroyAllWindows()
