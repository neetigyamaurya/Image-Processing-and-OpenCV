import cv2

# black = np.zeros((1000, 1000, 3), dtype=np.uint8)
# white = np.ones((1000, 1000, 3), dtype=np.uint8) * 255

# cv2.imwrite("Black.png", black)
# cv2.imwrite("White.png", white)

# Simple/Modulus addition
black = cv2.imread("images/Black.png")
white = cv2.imread("images/White.png")

result = (
    black + white
)  # This will cause a perfect modulus pixel by pixel addition can cause
# the image to overflow the 255 range
cv2.imshow("Simple Merged", result)

# cv2.add recommended method to add pixels will prevent the pixels f
# rom getting damaged
result_2 = cv2.add(black, white)  # Koi bhi image agge picche kar sakte hai
# results change nhi honge
cv2.imshow("CV2-Merged", result_2)
# cv2.addWeighted(img1,wt1,img2,wt2,gamma_val) This is the
# advanced version of cv2 add method
result_3 = cv2.addWeighted(black, 0.7, white, 0.3, 0)
cv2.imshow("Pro", result_3)
if cv2.waitKey(0) & 0xFF == ord("q"):
    print("DONE")
    print("EXITING")
    cv2.destroyAllWindows()
