import cv2

image_1 = cv2.imread('Firefly 20231001183002.png', 1)
image_2 = cv2.imread('Firefly neon sword on a black background 28217.jpg', 1)  # Isska size First image se
# chota hona chaiye
image_2_gray = cv2.cvtColor(image_2, cv2.COLOR_BGR2GRAY)
image_2_gray = cv2.resize(image_2_gray, (352, 352))
image_1 = cv2.resize(image_1, (900, 900))
image_2 = cv2.resize(image_2, (352, 352))
row, column, channels = image_2.shape
# ROI FOR IMAGE 1
# (547,279),(899,604) (y1,y2),(x1,x2)
roi = image_1[279:604, 547:899]
# Creating Threshold --mask
_, mask = cv2.threshold(image_2_gray, 100, 255, cv2.THRESH_BINARY)
# adaptive_mask = cv2.adaptiveThreshold(image_2_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)

# Remove Background
mask_inverted = cv2.bitwise_not(mask)


result = cv2.bitwise_and(roi, roi, mask=mask_inverted)
completed = cv2.add(result, image_1)
# PUT MASK INTO ROI
roi = cv2.bitwise_and(roi, roi, mask=mask_inverted)
cv2.imshow('inverted mask', mask_inverted)
cv2.imshow('simple mask', mask)
cv2.imshow('ROI', roi)
cv2.imshow('Image 1', image_1)
cv2.imshow('Image 2', image_2)
cv2.imshow('Image 2 Gray', image_2_gray)
# cv2.imshow('Adaptive', adaptive_mask)
cv2.imshow('Extracted', result)
cv2.imshow('Completed', completed)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows() 
