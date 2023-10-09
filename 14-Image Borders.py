import cv2
import numpy as np

img = np.zeros((500, 500, 3), dtype=np.uint8)
border = cv2.copyMakeBorder(
    img,
    10,
    10,
    20,
    20,
    cv2.BORDER_CONSTANT,
    value=[255, 255, 255],
)
cv2.imshow("Border", border)
if cv2.waitKey(0) & 0xFF == ord("q"):
    cv2.destroyAllWindows()
