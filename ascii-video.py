import time
import platform
import numpy as np
import cv2
import to_ascii


def main():
    window_name = "ASCII video"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, (600, 540))

    if platform.system() == 'Windows' and platform.release() == '10':
        cap = cv2.VideoCapture(cv2.CAP_DSHOW)
    else:
        cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,1)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1)

    # Framerate in frames per second.
    frame_rate = 5
    prev_time = 0

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False
    while ret:

        time_elapsed = time.time() - prev_time
        ret, frame = cap.read()

        # Stop capture if escape key pressed.
        if cv2.waitKey(1) == 27:
            break

        if time_elapsed > 1./frame_rate:
            prev_time = time.time()
            # Downscale captured frame to increase performance.
            downscaled = cv2.resize(frame, (120, 60), interpolation=cv2.INTER_LINEAR)
            size, data = to_ascii.img_to_ascii(downscaled)
            asciid = np.array(to_ascii.text_image(data))
            cv2.imshow(window_name, asciid)

    cv2.destroyWindow(window_name)

    cap.release()

if __name__ == '__main__':
    main()