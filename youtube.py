import cv2
import pafy

url = "https://www.youtube.com/watch?v=wIAs97ynODo&list=PLaHodugB5x-Ddy_H951h0VHjOjfzZNCBh&index=7"
data = pafy.new(url)
data = data.getbest(preftype="mp4")

cap = cv2.VideoCapture(data.url)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# Corrected the dimensions to (1280, 720)
output = cv2.VideoWriter("output.avi", fourcc, 24, (1280, 720))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("face", frame)
    output.write(frame)

    # Exit when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

output.release()
cap.release()
cv2.destroyAllWindows()
