import cv2
import numpy as np


def color_picker(event, x, y, flags, param):
    """This function is a callback for mouse events.
    It displays the color information
    of the pixel clicked on the image.

    Args:
        event (int): The type of mouse event.
        X (int): The x-coordinate of the mouse click.
        Y (int): The y-coordinate of the mouse click.
        Flags (int): Any flags associated with the event.
        param: Additional parameters (not used in this function).
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Access the color channels (BGR) of the pixel at (x, y)
        # Note: In OpenCV, image arrays are accessed as img[y, x]
        b = img[y, x, 0]  # Blue channel
        g = img[y, x, 1]  # Green channel
        r = img[y, x, 2]  # Red channel

        # Create a text string with the color information
        text = f"({b}, {g}, {r})"

        # Display the text on the image at the clicked coordinates
        cv2.putText(img, text, (x, y), font, 1, (255, 255, 255), 4, cv2.LINE_AA)

        # Print the color information to the console
        print(text)


# Create a named window for displaying the image
cv2.namedWindow("Image")

# Load an image from file
img = cv2.imread("/home/neetigya-maurya/Downloads/balls.jpg", 1)

# Set up the mouse callback function for the image window
while True:
    cv2.setMouseCallback("Image", color_picker)

    # Convert the image to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define lower and upper bounds for color masking (HSV values)
    lower_limit = np.array([16, 120, 72])
    upper_limit = np.array([60, 250, 87])

    # Create a mask to isolate the specified color range
    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    # Apply the mask to the original image to highlight the selected color
    filtered_image = cv2.bitwise_and(img, img, mask=mask)

    # Display the original image, mask, and filtered image
    cv2.imshow("Image", img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Filtered Image", filtered_image)

    # Check for user input to exit the loop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
