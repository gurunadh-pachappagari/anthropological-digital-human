import cv2
import imutils
import numpy as np


def outline(name):
    img = cv2.imread(str(name))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)

    _, gray = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)
    black = np.zeros(gray.shape)
    edges = cv2.Canny(gray, 50, 100)
    edges = cv2.dilate(edges, None, iterations=1)
    edges = cv2.erode(edges, None, iterations=1)

    cnt = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = imutils.grab_contours(cnt)

    cv2.drawContours(black, cnt, -1, 255, 1)

    return black


def show(thresh):
    cv2.imshow('Outline', thresh)
    cv2.waitKey(0)