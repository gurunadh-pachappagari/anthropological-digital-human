import cv2
import numpy as np


def face(front, side, top, center, lens):
    a1, a2 = lens[0]
    b1, b2 = lens[1]
    c1, c2 = lens[2]

    o1, o2, o3 = center

    # All the views are assumed to be ellipses and are draw using given lengths
    
    # front view

    cv2.ellipse(front, (o1, o2), (a1, b2), 0, 0, 90, 255, 1)
    cv2.ellipse(front, (o1, o2), (a2, b2), 0, 90, 180, 255, 1)
    cv2.ellipse(front, (o1, o2), (a2, b1), 0, 180, 270, 255, 1)
    cv2.ellipse(front, (o1, o2), (a1, b1), 0, 270, 360, 255, 1)

    # side view

    cv2.ellipse(side, (o3, o2), (c1, b2), 0, 0, 90, 255, 1)
    cv2.ellipse(side, (o3, o2), (c2, b2), 0, 90, 180, 255, 1)
    cv2.ellipse(side, (o3, o2), (c2, b1), 0, 180, 270, 255, 1)
    cv2.ellipse(side, (o3, o2), (c1, b1), 0, 270, 360, 255, 1)

    # top view

    cv2.ellipse(top, (o1, o3), (a1, c2), 0, 0, 90, 255, 1)
    cv2.ellipse(top, (o1, o3), (a2, c2), 0, 90, 180, 255, 1)
    cv2.ellipse(top, (o1, o3), (a2, c1), 0, 180, 270, 255, 1)
    cv2.ellipse(top, (o1, o3), (a1, c1), 0, 270, 360, 255, 1)


def neck(front, side, lens, center, face_lens):

    width, height, z = lens

    # The neck always starts from a particular point in the face ellipse so first the intercept is found the it is draw upto given height
    
    # front view

    tempx = center[0] - width//2
    node_2 = center[1] + face_lens[1][1]
    temp_arr = front[node_2:center[1]:-1, tempx]
    tempy = np.where(temp_arr == 255)[0][0]
    tempy = node_2 - tempy

    cv2.line(front, (tempx, tempy), (tempx, tempy+height), 255, 1)

    tempx = center[0] + width//2

    cv2.line(front, (tempx, tempy), (tempx, tempy + height), 255, 1)

    fendy = tempy + height

    # side view

    pivot = face_lens[2][0] + center[2]
    pt1 = (pivot, center[1])
    pt2 = (pivot, pt1[1] + face_lens[1][1] + height)

    cv2.line(side, pt1, pt2, 255, 1)

    tempx = pivot - z
    temp_arr = side[node_2:center[1]:-1, tempx]
    tempy = np.where(temp_arr == 255)[0][0]
    tempy = node_2 - tempy

    pt1 = (tempx, tempy)
    pt2 = (tempx, tempy+height)

    cv2.line(side, pt1, pt2, 255, 1)

    sendy = tempy + height

    return fendy, sendy


def torso(front, side, top, lens, center, pivot, o3, fendy, sendy):

    # The Chest, Hip and Stomach are all appoximated with a rectangle so the all us the same function torso 
    
    width, height, z = lens
    
    
    # front view

    pt1 = (center - width//2, fendy)
    pt2 = (pt1[0] + width, pt1[1] + height)

    cv2.rectangle(front, pt1, pt2, 255, 1)

    fendy = pt2[1]

    # side view

    pt1 = (pivot, sendy)
    pt2 = (pivot - z, sendy + height)

    cv2.rectangle(side, pt1, pt2, 255, 1)

    sendy = pt2[1]

    # top view

    pt1 = (center - width//2, o3 - height//2)
    pt2 = (pt1[0] + width, pt1[1] + height)

    cv2.rectangle(top, pt1, pt2, 255, 1)

    return fendy, sendy


def legs(front, side, lens, center, pivot, fendy, sendy, hip_lens):

    # legs is assumed to be a rectangle and is mirrored with respect to center by drawing only the left one.
    # in side view only one is draw
    
    width, height, z = lens

    pt1 = (center - hip_lens[0]//2, fendy)

    pt2 = (pt1[0] + width, pt1[1] + height)
    cv2.rectangle(front, pt1, pt2, 255, 1)

    mir_1 = (center + (center - pt1[0]), fendy)
    mir_2 = (center + (center - pt2[0]), pt2[1])

    cv2.rectangle(front, mir_1, mir_2, 255, 1)

    # side view

    pt1 = (pivot, sendy)
    pt2 = (pivot - z, sendy + height)

    cv2.rectangle(side, pt1, pt2, 255, 1)

    sendy = pt2[1]

    return fendy, sendy


def arms(front, side, top, lens, center, pivot, o3, a, b, chest_lens):

    # arms are drawn the same way as legs
    
    # front view

    c_w = chest_lens[0]
    c_z = chest_lens[2]
    width, height, z = lens
    pt1 = (center - c_w//2, a)
    pt2 = (pt1[0] - width, pt1[1] + height)
    cv2.rectangle(front, pt1, pt2, 255, 1)

    mir_1 = (center + (center - pt1[0]), pt1[1])
    mir_2 = (center + (center - pt2[0]), pt2[1])

    cv2.rectangle(front, mir_1, mir_2, 255, 1)

    # side view

    pt1 = (pivot, b)
    pt2 = (pivot - z, b + height)

    cv2.rectangle(side, pt1, pt2, 255, 1)

    # top view

    pt1 = (center - c_w//2, o3 - c_z//2)
    pt2 = (pt1[0] - width, pt1[1] - z)

    cv2.rectangle(top, pt1, pt2, 255, 1)

    mir_1 = (center + (center - pt1[0]), pt1[1])
    mir_2 = (center + (center - pt2[0]), pt2[1])

    cv2.rectangle(top, mir_1, mir_2, 255, 1)

