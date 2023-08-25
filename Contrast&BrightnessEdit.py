import cv2 as cv
import numpy as np

img = cv.imread('voi.jpg')
img = np.float32(img/255)
window = 'window'
contrast = 10
max_contrast = 100
brightness = 10
max_brightness = 100


def change_contrast(val):
    global contrast
    contrast = val/10
    perform_operation()


def change_brightness(val):
    global brightness
    brightness = val/100
    perform_operation()


def perform_operation():
    img1 = img * contrast + brightness
    cv.imshow(window, img1)


cv.imshow(window, img)
cv.createTrackbar("Contrast", window, contrast, max_contrast, change_contrast)
cv.createTrackbar("Brightness", window, brightness, max_brightness, change_brightness)
cv.waitKey(0)
