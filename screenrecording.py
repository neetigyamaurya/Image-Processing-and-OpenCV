import cv2  # OpenCV library for video capturing and processing
import numpy as np  # NumPy for array manipulation
import pyautogui  # PyAutoGUI for capturing screenshots and screen resolution

# Initialize the video capture object
cap = cv2.VideoCapture()

# Get screen resolution using pyautogui
screen_resolution = pyautogui.size()
print("Screen resolution:", screen_resolution)

# Prompt the user to enter the filename for the output video
filename = input("Enter the name of the File : ")
# Set frames per second (fps) for the video and choose the video codec
fps = 60
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# Create a VideoWriter object to save the screen recording
output = cv2.VideoWriter(filename, fourcc, fps, screen_resolution)

# Create a window for displaying the live screen recording
cv2.namedWindow("Screen Recording", cv2.WINDOW_NORMAL)

while True:
    # Capture the screen as an image using pyautogui
    screenshot = pyautogui.screenshot()

    # Convert the screenshot image to a NumPy array for OpenCV
    frame = np.array(screenshot)

    # Convert the color format from BGR to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the current frame to the output video file
    output.write(frame_rgb)

    # Display the live screen recording in a window
    cv2.imshow("Screen Recording", frame_rgb)

    # Check for the 'q' key press to stop the recording
    key = cv2.waitKey(24)
    if key == ord("q"):
        break

# Release resources and close the OpenCV window
output.release()
cap.release()
cv2.destroyAllWindows()

"""Here are explanations for the functions and libraries used:

cv2.VideoCapture(): Initializes a video capture object from the OpenCV library, which can be used to 
capture video frames from various sources like cameras or, in this case, the screen.

np.array(): Converts the screenshot captured by pyautogui into a NumPy array. 
NumPy is used for efficient array manipulation and processing.

cv2.cvtColor(): Converts the color format of the captured frame from BGR (Blue-Green-Red) 
to RGB (Red-Green-Blue) format. OpenCV represents images in BGR format by default, while 
most other libraries use RGB.

cv2.VideoWriter(): Creates a VideoWriter object that allows you to save video frames into 
a video file. It specifies the output filename, codec, frames per second, and screen resolution.

pyautogui.screenshot(): Captures a screenshot of the entire screen. PyAutoGUI is a library 
used for automating tasks, and in this case, it's used to capture the screen content.

cv2.imshow(): Displays the captured frame in an OpenCV window with the specified title.

cv2.waitKey(): Waits for a specified amount of time (given in milliseconds) for a 
keyboard event. It's used here to check if the 'q' key is pressed to stop the recording."""
