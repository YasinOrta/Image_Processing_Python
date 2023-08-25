import cv2 as cv


img = cv.imread("voi.jpg")
img = cv.resize(img, (1440, 900))

font = cv.FONT_HERSHEY_COMPLEX
cv.putText(img, "May the force be with you!", (250, 800), font, 2, (255, 255, 255), 3)

cv.imshow("window", img)

cv.waitKey(0)
cv.destroyAllWindows()
