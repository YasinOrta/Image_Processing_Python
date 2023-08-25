import cv2 as cv
import numpy as np


def nothing(x):
    pass


cv.namedWindow("Trackbar")
cv.createTrackbar("Threshold#1", "Trackbar", 0, 255, nothing)
cv.createTrackbar("Threshold#2", "Trackbar", 0, 255, nothing)

while True:


    img = cv.imread("coin4.jpg")
    img_original = img.copy()

    thresh1 = cv.getTrackbarPos("Threshold#1", "Trackbar")
    thresh2 = cv.getTrackbarPos("Threshold#2", "Trackbar")

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (15, 15), 0)
    edged = cv.Canny(blurred, thresh1, thresh2, 3)
    dilated = cv.dilate(edged, (1, 1), iterations=2)

    contours, hierarchy = cv.findContours(dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # Modify image shape for stacking
    gray = np.stack((gray,) * 3, axis=-1)
    blurred = np.stack((blurred,)*3, axis= -1)
    edged = np.stack((edged,)*3, axis= -1)
    dilated = np.stack((dilated,)*3, axis=-1)

    images = [gray, blurred, edged, dilated]
    win_names = ["Gray", "Blurred", "Edged", "Dilated"]

    font = cv.FONT_HERSHEY_SIMPLEX

    # vertical display of image array
    img_stack = np.vstack(images)
    for index, name in enumerate(win_names):
        image = cv.putText(img_stack, f'{index + 1}. {name}', (5, 30 + img.shape[0] * index),
                           font, 1, (205, 0, 255), 2, cv.LINE_AA)


    # horizontal display of image array
    """
    img_stack = np.vstack(images)
    for index, name in enumerate(win_names):
        image = cv.putText(img_stack, f'{index + 1}. {name}', (5 + img.shape[1] * index, 30),
                           font, 1, (205, 0, 255), 2, cv.LINE_AA)
    """

    # cv.imshow("Image Processing", img_stack)
    cv.drawContours(img, contours, -1, (0,0,255), 2)
    cv.imshow("Output", img)

    print("Coins in the image: ", len(contours))

    if cv.waitKey(0) & 0xFF == ord("x"):
        cv.destroyAllWindows()
