# Import necessary libraries
import cv2
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

# Open and load an image
image = Image.open('noise_intro_2.jpg')


# Function to resize the image while maintaining its aspect ratio
def resize(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    image_name = image.filename  # Get the image name
    resized_image.save(f"{image_name}")


# Resize the image to a specific width
resize(image, 700)

# Load the resized image and convert it to grayscale
image = cv2.imread('noise_intro_2.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -------------------------------------------Filter Number-1------------------------------------------------------------
# Apply a homogenous filter to the image, which is a simple averaging filter
# It replaces each pixel with the mean of its kernel neighbors
kernel = np.ones((5, 5), np.float32) / 25
homogenous_filter = cv2.filter2D(image, -1, kernel=kernel)  # -1 is the desired depth

# --------------------------------------------Filter Number-2----------------------------------------------------------
# Apply a blur filter (averaging) to the image
# It replaces each pixel with the average of the pixels in a defined kernel area
blur = cv2.blur(image, (5, 5))

# --------------------------------------------Filter Number-3-----------------------------------------------------------
# Apply a Gaussian blur filter to the image
# It uses a weighted kernel to smooth the image, giving more weight to nearby pixels
gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 0 is the sigma value

# --------------------------------------------Filter Number-4-----------------------------------------------------------
# Apply a median filter to the image
# It replaces each pixel with the median value of the pixels in a defined kernel area
median_blur = cv2.medianBlur(image, 5)

# --------------------------------------------Filter Number-5-----------------------------------------------------------
# Apply a bilateral filter to the image
# It is effective for noise removal while preserving edges
# Arguments: image, neighbor_pixel_diameter, sigma_color, sigma_space
bilateral_filter = cv2.bilateralFilter(image, 9, 75, 75)

# Display the original and filtered images
cv2.imshow('Original', image)
cv2.imshow('Homogenous Filter', homogenous_filter)
cv2.imshow('Blur', blur)
cv2.imshow('Gaussian', gaussian_blur)
cv2.imshow('Median', median_blur)
cv2.imshow('Bilateral', bilateral_filter)

# Create titles for the displayed images
titles = ['Original', 'Homogenous Filter', 'Blur', 'Gaussian', 'Median', 'Bilateral']
images = [image, homogenous_filter, blur, gaussian_blur, median_blur, bilateral_filter]

# Display images using Matplotlib
for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

# Show the plot
plt.show()

# Wait for a key press, and if 'q' is pressed, close all windows
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
