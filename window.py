import cv2
import numpy as np
import draws
from outline import outline
from controls import controller
import pickle


def run():

    flag = True
    hide = True
    view = 1

    with open('side_len.p', 'rb') as fp:
        lens = pickle.load(fp)

    img = outline('man_2.jpg')
    simg = outline('side.jpg')

    while flag:
        if hide:
            front = np.zeros((500, 480))
            side = np.zeros((500, 480))
        else:
            front = img.copy()
            side = simg.copy()

        top = np.zeros((480, 480))

        display(front, side, top, lens)

        flag, hide, view = controller(lens, flag, hide, view)


def display(front, side, top, lens):

    center = lens['center']
    pivot = lens['face'][2][0] + lens['center'][2]

    draws.face(front, side, top, center, lens['face'])
    fendy, sendy = draws.neck(front, side, lens['neck'], center, lens['face'])

    a = fendy
    b = sendy

    fendy, sendy = draws.torso(front, side, top, lens['chest'], center[0], pivot, center[2], fendy, sendy)
    fendy, sendy = draws.torso(front, side, top, lens['stomach'], center[0], pivot, center[2], fendy, sendy)
    fendy, sendy = draws.torso(front, side, top, lens['hip'], center[0], pivot, center[2], fendy, sendy)

    draws.legs(front, side, lens['legs'], center[0], pivot, fendy, sendy, lens['hip'])
    draws.arms(front, side, top, lens['arms'], center[0], pivot, center[2], a, b, lens['chest'])

    cv2.imshow('front', front)
    cv2.imshow('side', side)
    # cv2.imshow('top', top)
    cv2.waitKey(2000)


run()

# nodes = np.array([[240, 11], [213, 43], [240, 69], [262, 45],
#                  [224, 76], [180, 85], [190, 154], [192, 202],
#                  [192, 249], [228, 453],
#                  [50, 112]])  # hands
