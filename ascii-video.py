import cv2
import numpy as np
import time
import to_ascii


'''
https://stackoverflow.com/questions/10965417/how-to-convert-a-numpy-array-to-pil-image-applying-matplotlib-colormap
https://stackoverflow.com/questions/17856242/convert-string-to-image-in-python
'''


def main():
    window_name = "Window 1"
    frame_rate = 5
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, (600, 600))
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,50)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,50)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    prev = 0

    while ret:

        time_elapsed = time.time() - prev
        ret, frame = cap.read()

        # Stop capture if escape key pressed
        if cv2.waitKey(1) == 27:
            break

        if time_elapsed > 1./frame_rate:
            prev = time.time()
            size, data = to_ascii.img_to_ascii(frame)
            asciid = np.array(to_ascii.text_image(data))
            cv2.imshow(window_name, asciid)

    cv2.destroyWindow(window_name)

    cap.release()

if __name__ == '__main__':
    main()