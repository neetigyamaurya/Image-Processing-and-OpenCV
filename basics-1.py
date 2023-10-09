import cv2

img = cv2.imread("/home/neetigya-maurya/Pictures/COMPARE.jpg", 0)
print(img)
print(img.shape)
while True:
    k = cv2.waitKey(30)
    if k == ord("q") & 0xFF:
        cv2.destroyAllWindows()
    elif k == ord("s") & 0xFF:
        img = cv2.flip(img, -1)
        cv2.imwrite("/home/neetigya-maurya/Pictures/COMPARE-Flipped.jpg", img)
        cv2.destroyAllWindows()
    else:
        cv2.imshow("Image", img)
