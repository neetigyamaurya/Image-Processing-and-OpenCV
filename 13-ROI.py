import cv2


def mouse_event(event, x, y, flags, param):
    font = cv2.FONT_HERSHEY_SIMPLEX
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates = str(x) + "," + str(y)
        cv2.putText(img, coordinates, (x, y), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
        print((x, y))


img = cv2.imread("/home/neetigya-maurya/Pictures/IMG_20230325_121359836.jpg")
img = cv2.resize(img, (1000, 1000))
roi = img[328:788, 200:672]  # (y1:y2),(x1:x2))
img[328:788, 528:1000] = roi
img[540:1000, 200:672] = roi
cv2.namedWindow("COMPARE_BW")
cv2.setMouseCallback("COMPARE_BW", mouse_event)
while True:
    cv2.imshow("COMPARE_BW", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

# ROI
# (200,328)(672,788)
