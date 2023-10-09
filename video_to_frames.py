import cv2

# Initialize a counter to keep track of frames
count = 0

# Open the video file for reading
cap = cv2.VideoCapture("extract-2.mp4")

# Read the first frame from the video
ret, frame = cap.read()

# Loop until the video is opened and frames are available
while cap.isOpened():
    # Print whether the video capture is open (True) or closed (False)
    print(cap.isOpened())

    # Increment the frame counter
    count += 1

    # Read the next frame from the video
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if ret:
        # Check if the frame is not empty and has some size
        if not frame is None and not frame.size == 0:
            # Save the frame as an image with a filename based on the frame count
            cv2.imwrite(f"frames/{count}.jpg", frame)

            # Set the video capture position to a specific time (100 milliseconds times the frame count)
            cap.set(cv2.CAP_PROP_POS_MSEC, (count * 100))

            # Display the frame in a window named "frame"
            cv2.imshow("frame", frame)

            # Wait for 40 milliseconds and check if the 'q' key is pressed
            key = cv2.waitKey(40)

            # If 'q' is pressed, release the video capture and close the window
            if key == ord("q"):
                cap.release()
                cv2.destroyAllWindows()
