import cv2
import imutils
import numpy as np


def outline(name):
    img = cv2.imread(str(name))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0) # A Gaussian Blur with 7x7 kernal

    _, gray = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY) # and pixel value aboue 220 is taken a 255 and below is taken as 0
    black = np.zeros(gray.shape) # black background
    edges = cv2.Canny(gray, 50, 100) # This is a edge detection algorithm
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1) 
    # dilation and erosion removes noise

    cnt = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = imutils.grab_contours(cnt)

    cv2.drawContours(black, cnt, -1, 255, 1)
    # finally the contours are found and drawn over black background.

    return black


def show(thresh):
    cv2.imshow('Outline', thresh)
    cv2.waitKey(0)
