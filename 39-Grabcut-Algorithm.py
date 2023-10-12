"""The GrabCut algorithm in a simple way.

Imagine you have a picture, like a coloring book page, and you want to color just one thing in it, like a dog.
But there are other things in the picture, like a cat and a tree; that you don't want to color.
GrabCut is like a magic tool that helps you do this.

Here's how it works:

1. First, you draw a rectangle around the dog with your magic tool. This tells GrabCut where the dog is.

2. Then, you tell GrabCut which parts of the picture are the dog (the part you want to color) and which parts are the
background (the things you don't want to color).

3. GrabCut will start working its magic. It looks at the colors and shapes inside the rectangle you drew and figures
out which parts are probably the dog and which parts are probably the background.

4. It keeps doing this over and over, making the rectangle smaller and smaller until it's perfect for knowing what's
the dog and what's the background.

5. Now, you can color just the dog, and the magic tool makes sure you don't color the cat or the tree by mistake.

So, in simple words, GrabCut helps you separate the things you want to color from the things you don't want to color in
 a picture, almost like magic!"""

# Gaussian mixture model is used to achieve this target.
# Import necessary tools
import cv2  # This helps us work with pictures
import numpy as np  # This helps us do math


# Function to resize the image while keeping its shape
# Imagine making a big picture smaller
def resize(image, new_height):
    # Figure out how wide the picture should be to keep it looking nice
    h, w = image.shape[:2]  # This tells us the picture's height and width
    ratio = float(w) / float(h)  # Imagine the picture's width compared to its height
    new_width = int(ratio * new_height)  # This is how wide the picture should be
    resized_image = cv2.resize(image, (new_width, new_height))  # Make the picture the right size
    return resized_image  # Get the new, smaller picture


# Load the image (a picture of a car) and make it a bit smaller
image = cv2.imread('images/Toyota yaris.jpg')  # Get the picture
image = resize(image, 800)  # Make it a good size for us to work with

# Prepare models for GrabCut (background and foreground)
# Think of these as special tools to help us separate the car from the background
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Create a mask to specify the regions of the image
# Imagine this mask as a coloring book where we'll say which parts are the car (to color) and which parts are the
# background (to leave blank)
mask = np.zeros(image.shape[:2], np.uint8)

# Define a rectangle around the object you want to separate (in this case, the car)
# Picture a box around the car to tell the computer where the car is
rect = (107, 91, 1020, 647)  # The rectangle's position and size

# Use GrabCut to separate the car from the background
# Imagine a magic tool that looks at the picture and separates the car from the rest
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)

# Create a new mask where car pixels are marked as 1 and the background as 0
# Think of this like a magic eraser, keeping only the car and removing everything else
mask_2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

# Apply the mask to the image, showing only the car
# This is like painting the car but leaving the rest of the picture blank
image = image * mask_2[:, :, np.newaxis]

# Show the original image with just the car
# We see the car, and everything else is gone
cv2.imshow('Original', image)

# Show the mask where the car is marked as 1
# The mask shows where we colored (the car) and where we didn't (the background)
cv2.imshow('Mask 2', mask_2)

# Wait for a key press and then close the windows when 'q' is pressed
# We can press 'q' to finish and see our cool picture
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
'''In the code snippet `mask = np.zeros(image.shape[:2], np.uint8)`, we are creating an empty mask, which is 
like a template that will help us mark which parts of the image belong to the foreground (in this case, the car) 
and which parts belong to the background.

1. `image.shape[:2]` tells us the height and width of the picture. It's like knowing how tall and wide the coloring 
book page is.

2. `np.zeros(...)` creates a blank coloring book page with the same height and width as our picture. Everything on 
this page starts out empty (just like a page with no colors yet).

3. `np.uint8` tells us that we'll use small numbers to mark things on our coloring book page. It's like 
saying we'll use little dots to color.

So, when we run `mask = np.zeros(image.shape[:2], np.uint8)`, it's like giving us a blank coloring book page 
that's the same size as our picture, and we'll use tiny dots to mark where the car is (the foreground) and where 
it isn't (the background). We'll fill in this "coloring book" later to separate the car from the rest of the picture.


In the code snippet:

```python
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
```

We are creating two special models to help us with the GrabCut algorithm. These models are like tools that the algorithm
 uses to figure out what's the foreground (the car) and what's the background (everything else). Let's break it down:

1. `bgd_model` and `fgd_model` are the names of these models. They are like two sets of instructions that GrabCut 
follows.

2. `np.zeros(...)` is used to create an empty set of instructions. It's like having a blank piece of paper with nothing 
written on it.

3. `(1, 65)` tells us the size of the paper. It's like saying our instructions will have 65 slots, and we have 1 piece 
of paper for each model.

4. `np.float64` is a way to say that our instructions will use numbers with decimal points, like 1.0, 2.5, etc. It's 
like saying we can use fractions.

So, when we write `bgd_model = np.zeros((1, 65), np.float64)` and `fgd_model = np.zeros((1, 65), np.float64)`, we are 
preparing two sets of instructions, one for the background and one for the foreground, with 65 slots each, but they 
start empty. Later in the GrabCut process, GrabCut will fill in these slots with information about what's the car and 
what's the background. These models help GrabCut do its magic and separate the car from the background.
The `bgd_model` and `fgd_model` having the shape (1, 65) in the GrabCut algorithm is a requirement of the 
OpenCV library. This shape is specific to the OpenCV implementation of GrabCut. Let me explain why it has this shape:

1. **(1, 65) Shape**: In the context of GrabCut, each of these models contains parameters related to the pixel 
classification, such as the probability that a pixel belongs to the background or foreground. The shape (1, 65) 
is used to store these parameters, and it's designed to accommodate different types of information.

2. **65 Parameters**: The 65 parameters are used to represent various statistics and probabilities related to pixel 
classification. These include mean and covariance values for both foreground and background, as well as other 
statistical information used for classification. Essentially, it stores a mixture of Gaussian distributions to model 
the pixel colors in the image.

3. **Why (1, 65)**: The (1, 65) shape is used to maintain compatibility with the way OpenCV handles the parameters. 
The "1" is there because it signifies that there is a single model (it doesn't vary with multiple objects), and the 
"65" is the number of parameters used to represent the pixel information.

In simpler terms, think of the (1, 65) shape as a special container that holds all the important information the 
algorithm needs to distinguish between the foreground (the object we want to isolate) and the background. It's a 
standardized format used in OpenCV for this specific task.
In the code snippet:

```python
cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)
```

We are using the OpenCV library's GrabCut function to perform the magic separation of the car from the background. 
Let's break it down step by step:

1. `cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)` is like telling the computer to 
work its magic to separate the car from the rest of the picture.

2. `image` is the picture we want to work with, which contains the car and the background.

3. `mask` is our coloring book or "coloring guide," where we indicate which parts are the car and which are the
 background. It helps GrabCut know what we want to separate.

4. `rect` is like a rectangle drawn around the car in the image. It helps GrabCut understand where the car is located.

5. `bgd_model` and `fgd_model` are special sets of instructions (like notes or clues) that GrabCut uses to figure out 
what's the car and what's the background. These models were prepared earlier.

6. `10` is a number that tells GrabCut how many times it should repeat its magic to get better at separating the car 
from the background. The more times it repeats, the more accurate the separation becomes.

7. `cv2.GC_INIT_WITH_RECT` is like saying we're starting the separation with the rectangle we drew around the car.

So, when we run `cv2.grabCut(image, mask, rect, bgd_model, fgd_model, 10, cv2.GC_INIT_WITH_RECT)`, we are telling the 
computer to perform the GrabCut magic using our picture, coloring guide, and models, starting with the car's rectangle.
 It will do this several times to make sure it gets the best separation between the car and the background.'''
