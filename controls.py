import numpy as np
import pickle


def controller(main_lens, end, hide, view):

    lens = finder(view, main_lens)
    solve = True
    control = input().split()
    if 0 < len(control) <= 2:
        if control[0] == 'end':
            end = False

        elif control[0] == 'save':
            with open(control[1]+'.p', 'wb') as fp:
                pickle.dump(main_lens, fp, protocol=pickle.HIGHEST_PROTOCOL)

        elif control[0] == 'load':
            with open(control[1]+'.p', 'rb') as fp:
                main_lens = pickle.load(fp)

        elif control[0] == 'hide':
            hide = True
        elif control[0] == 'show':
            hide = False
        elif control[0] == 'front':
            view = 1
            solve = False
        elif control[0] == 'side':
            view = 2
            solve = False
        elif control[0] == 'top':
            view = 3
            solve = False
        else:
            print("INVALID INPUT")

    elif len(control) == 3:

        if control[0] == 'center':
            lens['center'][0] += int(control[1])
            lens['center'][1] += int(control[2])
        elif control[0] == 'face':
            if control[1] == '1':
                lens['face'][1][0] += int(control[2])
            elif control[1] == '2':
                lens['face'][0][1] += int(control[2])
            elif control[1] == '3':
                lens['face'][1][1] += int(control[2])
            elif control[1] == '4':
                lens['face'][0][0] += int(control[2])
        else:
            parts = {'neck', 'chest', 'stomach', 'hip', 'legs', 'arms'}
            if control[0] in parts:
                lens[control[0]][int(control[1]) - 1] += int(control[2])
            else:
                print("INVALID INPUT")
    else:
        print("INVALID INPUT")

    if solve:
        main_lens = solver(view, main_lens, lens)

    return end, hide, view


def finder(view, lens):

    new_lens = dict()

    if view == 1:
        i, j = 0, 1
    elif view == 2:
        i, j = 2, 1
    else:
        i, j = 0, 2

    for s in lens:
        new_lens[s] = [lens[s][i], lens[s][j]]

    return new_lens


def solver(view, main, lens):

    if view == 1:
        i, j = 0, 1
    elif view == 2:
        i, j = 2, 1
    else:
        i, j = 0, 2

    for s in lens:
        main[s][i] = lens[s][0]
        main[s][j] = lens[s][1]

    return main

