import cv2 as cv
import numpy as np


def empty_function():
    pass


def main():
    image = np.zeros((512, 512, 3), np.uint8)
    window_name = "Open CV Color Palette"

    cv.namedWindow(window_name)

    cv.createTrackbar('Blue', window_name, 0, 255, empty_function)
    cv.createTrackbar('Green', window_name, 0, 255, empty_function)
    cv.createTrackbar('Red', window_name, 0, 255, empty_function)

    while True:
        cv.imshow(window_name, image)

        if cv.waitKey(1) == 27:
            break

        blue = cv.getTrackbarPos('Blue', window_name)
        green = cv.getTrackbarPos('Green', window_name)
        red = cv.getTrackbarPos('Red', window_name)

        image[:] = [blue, green, red]
        print(blue, green, red)

    cv.destroyAllWindows()


# Calling main()
if __name__ == "__main__":
    main()
