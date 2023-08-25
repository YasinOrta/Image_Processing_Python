import cv2 as cv


def change(x):
    pass


cv.namedWindow("redCar")
cv.resizeWindow("redCar", 300, 100)
cv.createTrackbar("width", "redCar", 100, 1440, change)
cv.createTrackbar("height", "redCar", 100, 900, change)

while True:
    width = cv.getTrackbarPos("width", "redCar")
    height = cv.getTrackbarPos("height", "redCar")

    image = cv.imread("voi.jpg")
    image = cv.resize(image, (width, height))
    cv.imshow("Car", image)

    if cv.waitKey(1) & 0xFF == ord("x"):
        cv.destroyAllWindows()
