import cv2

URL = "http://192.168.1.35:8080/video"


def maintain_aspect_ratio_resize(frame, width=1500):
    aspect_ratio = frame.shape[1] / float(frame.shape[0])
    height = int(width / aspect_ratio)
    return cv2.resize(frame, (width, height))


def get_netcam_data(url):
    cap = cv2.VideoCapture(url)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    output = cv2.VideoWriter(
        "/home/neetigya-maurya/Programming/Python/OpenCv/record.mp4",
        fourcc,
        30,
        (int(cap.get(3)), int(cap.get(4))),  # Use the dimensions of the captured video
    )

    while cap.isOpened():
        ret, frames = cap.read()
        if ret:
            if frames is not None and frames.size != 0:
                frames = maintain_aspect_ratio_resize(frames)
                output.write(frames)
                print("Writing frames")
                cv2.imshow(f"{url}", frames)
                if cv2.waitKey(24) == ord("q"):
                    output.release()
                    cap.release()
                    cv2.destroyAllWindows()
            else:
                print("Error while reading")
                break


get_netcam_data(URL)
