import cv2
import numpy as np

front = top = side = np.zeros((500, 480))


def face(front, center, lengths, color):

    a ,b1, b2 = lengths
    nodes = {
        'center': tuple(center),
        'node_1': (center[0], center[1]-b1),
        'node_2': (center[0]-a//2, center[1]),
        'node_3': (center[0], center[1]+b2),
        'node_4': (center[0]+a//2, center[1])
    }

    cv2.ellipse(front, nodes['center'], (a, b1), 180, 0, 180, color, 1)
    cv2.ellipse(front, nodes['center'], (a, b2), 0, 0, 180, color, 1)
    
    return nodes


def face_control():

    center = [240, 50]
    lengths = [40, 50, 44]
    while True:
        nodes = face(front, center, lengths, 255)
        cv2.imshow('front', front)
        cv2.waitKey(3000)
        nodes = face(front, center, lengths, 0)
        control = input().split()
        if control[0] == 'center':
            center[0] += int(control[1])
            center[1] += int(control[2])
        elif control[0] == 'node':
            if control[1] == '1':
                lengths[1] += int(control[2])
            elif control[1] == '2' or control[1] == '4':
                lengths[0] += int(control[2])
            elif control[1] == '3':
                lengths[2] += int(control[2])
            else:
                break
        elif control[0] == 'end':
            break
        else:
            break
    
    return nodes


def neck(front, node_2, node_3):
    lengths = [30, 15]
    temp = node_3[0]-lengths[0]//2
    j = -1
    for j in range(node_3[1], node_2[1], -1):
        if front[j][temp] == 255:
            break
    if j != -1:
        pt1 = (temp, j)

    temp = node_3[0] + lengths[0] // 2
    j = -1
    for j in range(node_3[1], node_2[1], -1):
        if front[j][temp] == 255:
            break
    if j != -1:
        pt2 = (temp, j)

    cv2.line(front, pt1, pt2, 255, 1)


nodes = face_control()