import cv2

img = cv2.imread("/home/neetigya-maurya/Pictures/eleaves.jpg")
img = cv2.resize(img, (1280, 720))
print("Image shape:", img.shape)
print("Number of Pixels: ", img.size)
cv2.imshow("COMPARE_BW", img)
print("Image Datatype", img.dtype)
b, g, r = cv2.split(img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)
merge = cv2.merge((r, g, b))
cv2.imshow("Merged", merge)
# Acess pixel with coordinates
px = img[52, 52]
print(px)
px = img[52, 52, 0]  # This will get the blue pixel
print(f"Blue Pix: {px}")
px = img[52, 52, 1]  # This will get the green pixel
print(f"Green Pix: {px}")
px = img[52, 52, 2]  # This will get the red pixel
print(f"Red Pix: {px}")
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
