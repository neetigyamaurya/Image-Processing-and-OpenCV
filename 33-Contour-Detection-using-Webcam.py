import cv2
import numpy as np

# Open the default camera (usually the webcam)
cap = cv2.VideoCapture(0)


# Define a callback function for trackbars (not used in this code)
def nothing(x):
    pass


# Create a window for adjusting HSV parameters
cv2.namedWindow("HSV Adjustment", cv2.WINDOW_NORMAL)
cv2.resizeWindow("HSV Adjustment", (300, 300))

# Create trackbars for adjusting HSV thresholds and bounds
cv2.createTrackbar("Threshold", "HSV Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower Hue", "HSV Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower Saturation", "HSV Adjustment", 0, 255, nothing)
cv2.createTrackbar("Lower Value", "HSV Adjustment", 0, 255, nothing)
cv2.createTrackbar("Upper Hue", "HSV Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper Saturation", "HSV Adjustment", 255, 255, nothing)
cv2.createTrackbar("Upper Value", "HSV Adjustment", 255, 255, nothing)

# Start capturing and processing video frames
while cap.isOpened():
    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        # Resize the frame and flip horizontally for better viewing
        frame = cv2.resize(frame, (400, 400))
        frame = cv2.flip(frame, 1)

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Get lower and upper HSV bounds from trackbars
        l_hue = cv2.getTrackbarPos("Lower Hue", "HSV Adjustment")
        l_sat = cv2.getTrackbarPos("Lower Saturation", "HSV Adjustment")
        l_val = cv2.getTrackbarPos("Lower Value", "HSV Adjustment")
        u_hue = cv2.getTrackbarPos("Upper Hue", "HSV Adjustment")
        u_sat = cv2.getTrackbarPos("Upper Saturation", "HSV Adjustment")
        u_val = cv2.getTrackbarPos("Upper Value", "HSV Adjustment")

        lower_bound = np.array([l_hue, l_sat, l_val])
        upper_bound = np.array([u_hue, u_sat, u_val])

        # Create a binary mask based on the HSV bounds
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        # Get the threshold value from the trackbar
        thresh_value = cv2.getTrackbarPos("Threshold", "HSV Adjustment")

        # Apply binary thresholding to the mask
        ret, threshold = cv2.threshold(mask, thresh_value, 255, cv2.THRESH_BINARY)

        # Perform morphological operations (opening) to reduce noise
        kernel = np.array((3, 3), np.uint8)
        opening = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

        # Apply bilateral filtering to reduce noise further
        bilateral_filter = cv2.bilateralFilter(opening, 9, 75, 75)

        # Apply median blur to further reduce noise
        median_blur = cv2.medianBlur(bilateral_filter, 5)

        # Find contours in the processed image
        contours, hierarchy = cv2.findContours(median_blur, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours and convex hulls on the original frame
        for c in contours:
            epsilon = 0.0001 * cv2.arcLength(c, True)
            data = cv2.approxPolyDP(c, epsilon, True)
            hull = cv2.convexHull(data)
            cv2.drawContours(frame, [c], -1, (0, 0, 255), 4)
            cv2.drawContours(frame, [hull], -1, (0, 255, 255), 2)

        # Display various processed images and the original frame
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", frame)
        cv2.imshow("Threshold", threshold)
        cv2.imshow("Opening", opening)
        cv2.imshow("Median Blur", median_blur)

        # Press 'q' to exit the loop and close all windows
        if cv2.waitKey(1) == ord("q"):
            cap.release()
            cv2.destroyAllWindows()  # Close all windows before breaking the loop
            break

# Close any open windows when the loop is done
cv2.destroyAllWindows()
