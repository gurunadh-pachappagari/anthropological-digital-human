import numpy as np
import cv2


def face(side, o2, o3, b1, b2, c1, c2):
    cv2.ellipse(side, (o3, o2), (c1, b2), 0, 0, 90, 255, 1)
    cv2.ellipse(side, (o3, o2), (c2, b2), 0, 90, 180, 255, 1)
    cv2.ellipse(side, (o3, o2), (c2, b1), 0, 180, 270, 255, 1)
    cv2.ellipse(side, (o3, o2), (c1, b1), 0, 270, 360, 255, 1)

def neck(side, length, width, z, center, face_lens):


