import numpy as np
import pickle

# A simple UI to test the working of the algorithm 

def controller(main_lens, end, hide, view):

    lens = finder(view, main_lens) # depending on the view the required 2-D lengths are taken from a 3D lengths matrix
    solve = True # to affect the changes made
    control = input().split()
    if 0 < len(control) <= 2:
        if control[0] == 'end': # To end the program
            end = False

        elif control[0] == 'save': # To save a template
            with open(control[1]+'.p', 'wb') as fp:
                pickle.dump(main_lens, fp, protocol=pickle.HIGHEST_PROTOCOL)

        elif control[0] == 'load': # To load a template
            with open(control[1]+'.p', 'rb') as fp:
                main_lens = pickle.load(fp)

        elif control[0] == 'hide': # To hide the image
            hide = True
        elif control[0] == 'show': # to show the image
            hide = False
        elif control[0] == 'front': # to change view to front
            view = 1
            solve = False
        elif control[0] == 'side': # to change view to side
            view = 2
            solve = False
        elif control[0] == 'top': # to change view to top
            view = 3
            solve = False
        else:
            print("INVALID INPUT")

    elif len(control) == 3: # to update the template

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
        main_lens = solver(view, main_lens, lens) # to update the 3-D lengths from the changed 2-D lengths

    return end, hide, view


def finder(view, lens): # coverted 3-D lengths to specific 2-D lengths

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


def solver(view, main, lens): # To convert back from specific 2-D lengths to 3-D lengths.

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

