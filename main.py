import numpy as np
import random
import astar as astar
import pyraminx as pyraminx
import timeit



def rotate90(masterPyraminx, face):  # rotation in the left direction if facing towards you
    temps = masterPyraminx[int(face)]
    if face == 3:
        newFace = [[temps[0][6], temps[0][5], temps[1][4], temps[1][3], temps[2][2], temps[2][1], temps[3][0]],  # bottom front row
                   [temps[0][4], temps[0][3], temps[1]
                       [2], temps[1][1], temps[2][0]],
                   [temps[0][2], temps[0][1], temps[1][0]],
                   [temps[0][0]]]
    else:
        newFace = [

            [temps[3][6]],
            [temps[2][4], temps[3][5], temps[3][4]],
            [temps[1][2], temps[2][3], temps[2][2], temps[3][3], temps[3][2]],
            [temps[0][0], temps[1][1], temps[1][0], temps[2][1], temps[2][0], temps[3][1], temps[3][0]], ]

    masterPyraminx[int(face)] = newFace
    return newFace


def moveHorizontal(masterPyraminx, direction, layer):
    print(f"this is the inputted direction {direction}")
    layer = int(layer)
    directionDict = {0: 1, 1: (-1)}
    for index in range(0, layer+1):
        print(f"this is the index {index} and this is the layer {layer}")
        listToMove = [masterPyraminx[0][index],
                      masterPyraminx[1][index], masterPyraminx[2][index]]
        print(f"list to move {listToMove}")
        movedList = np.roll(listToMove, len(
            listToMove[0])*directionDict.get(direction))
        for i in range(len(movedList)):
            masterPyraminx[i][index] = list(movedList[i])
        rotateDirection = {'r': 3, 'l': 2}
        # if layer == 3:
        #     for i in range(0, rotateDirection.get(direction)):
        #         rotate90(masterPyraminx, 3)

    return


def leftToBottom(face):
    newFace = [
        [face[0][0], face[1][1], face[1][2], face[2][3], face[2]
            [4], face[3][5], face[3][6]],  # bottom front row
        [face[1][0], face[2][1], face[2][2], face[3][3], face[3][4]],
        [face[2][0], face[3][1], face[3][2]],
        [face[3][0]]
    ]
    return newFace


def rightToBottom(face):
    newFace = [
        [face[3][0], face[3][1], face[2][0], face[2][1], face[1]
            [0], face[1][1], face[0][0]],  # bottom front row
        [face[3][2], face[3][3], face[2][2], face[2][3], face[1][2]],
        [face[3][4], face[3][5], face[2][4]],
        [face[3][6]]
    ]
    return newFace


def bottomToTop(face):
    newFace = [

        [face[3][0]],
        [face[2][2], face[2][1], face[2][0]],
        [face[1][4], face[1][3], face[1][2], face[1][1], face[1][0]],
        [face[0][6], face[0][5], face[0][4], face[0][3], face[0][2], face[0][1], face[0][0]], ]
    return newFace


def bottomToTopLeft(face):
    newFace = [

        [face[0][0]],
        [face[1][0], face[0][1], face[0][2]],
        [face[2][0], face[1][1], face[1][2], face[0][3], face[0][4]],
        [face[3][0], face[2][1], face[2][2], face[1][3], face[1][4], face[0][5], face[0][6]], ]
    return newFace

def orientL(masterPyraminx):
    temp = [masterPyraminx[0], masterPyraminx[1],
            masterPyraminx[2], masterPyraminx[3]]
    masterPyraminx[0] = rotate90(temp, 0)
    masterPyraminx[0] = rotate90(masterPyraminx, 0)
    masterPyraminx[1] = rotate90(temp, 2)
    masterPyraminx[2] = bottomToTopLeft(temp[3])
    masterPyraminx[3] = rightToBottom(temp[1])
    return


def orientR(masterPyraminx):
    temp = [masterPyraminx[0], masterPyraminx[1],
            masterPyraminx[2], masterPyraminx[3]]
    masterPyraminx[0] = rotate90(temp, 0)
    masterPyraminx[1] = bottomToTop(temp[3])
    masterPyraminx[2] = rotate90(temp, 1)
    masterPyraminx[3] = leftToBottom(temp[2])
    return


def orientB(masterPyraminx):
    temp = [masterPyraminx[0], masterPyraminx[1],
            masterPyraminx[2], masterPyraminx[3]]
    masterPyraminx[0] = rotate90(temp, 2)
    masterPyraminx[0] = rotate90(masterPyraminx, 0)
    masterPyraminx[1] = rotate90(temp, 1)
    masterPyraminx[2] = bottomToTop(temp[3])
    masterPyraminx[3] = rightToBottom(temp[0])
    return


def randomizer(numMoves):
    moves = ['U', 'L', 'R', 'B', 'Uw', 'Lw', 'Rw', 'Bw', 'u', 'l', 'r', 'b']
    movesList = []
    for i in range(0, numMoves):
        movesList.append(random.choice(moves))
    return movesList


def orient(masterPyraminx, orientation):
    if orientation == 0:    # U moving the front no re-orientation needed
        print(orientation)
    elif orientation == 1:  # L moving the left, need to rotate up to the right
        print(orientation)
        orientL(masterPyraminx)
    elif orientation == 2:  # R moving the right, need to rotate up to the left
        print(orientation)
        orientR(masterPyraminx)
    elif orientation == 3: # B moving the back, need to rotate up and left or right. we will choose right.
        print(orientation)
        orientB(masterPyraminx)
    return


def getGameMode():
    masterPyraminx = pyraminx.Pyraminx().masterPyraminx
    names = ['front', 'right', 'left', 'bottom']
    for i in range(len(masterPyraminx)):
        print(names[i])
        print(str(masterPyraminx[i]).replace(
            '], ', ',\n ').replace('[', '').replace(']]', ''))
    gameOn = True
    while gameOn == True:
        playMode = input(
            "press r to randomize or m to manually play or q to quit: ")
        if playMode == 'r':
            numMoves = input("how many moves would you like to simulate: ")
            movesList = randomizer(int(numMoves))
            print(f"this is moveslist = {movesList}")
            playGame(movesList, masterPyraminx, 0)
            answer = False
            while answer == False:
                solveOption = input("would you like to auto-solve?(y/n): ")
                if solveOption == 'y':
                    print("begin attempt")
                    start = timeit.default_timer()
                    solvedPyraminx = pyraminx.Pyraminx().masterPyraminx
                    unsolvedPyraminx = masterPyraminx
                    print(f"solved = {solvedPyraminx}")
                    print(f"unsolved = {unsolvedPyraminx}")
                    path = astar.astar(unsolvedPyraminx, unsolvedPyraminx,solvedPyraminx,numMoves)
                    stop = timeit.default_timer()
                    print('Time: ', stop - start)  
                    print(len(path))
                    print("have a nice day!")
                    exit()
                else:
                    print("thank you have a nice day")
                    exit()
        elif playMode == 'm':
            numMoves = 0
            choice = [input('what move do you want to make?: ')]
            while choice != 'q':
                numMoves=numMoves+1
                print(f"checking {choice}")
                if choice[0] == 's':
                    print("begin attempt")
                    start = timeit.default_timer()
                    solvedPyraminx = pyraminx.Pyraminx().masterPyraminx
                    unsolvedPyraminx = masterPyraminx
                    print(f"solved = {solvedPyraminx}")
                    print(f"unsolved = {unsolvedPyraminx}")
                    path = astar.astar(unsolvedPyraminx, unsolvedPyraminx,solvedPyraminx,numMoves)
                    stop = timeit.default_timer()
                    print('Time: ', stop - start)  
                    # print(path)
                    print("have a nice day!")
                    exit()
                playGame(choice, masterPyraminx, 0)
                choice = [input('what move do you want to make?: ')]


        elif playMode == 'q':
            return False
    return True


def playGame(choices, masterPyraminx, direction):
    # only counterclockwise (from top down) moves allowed for randomizer, clockwize for solver (doing same move twice vs once)
    layer0 = ['U', 'L', 'R', 'B']
    layer1 = ['Uw', 'Lw', 'Rw', 'Bw']
    layer2 = ['u', 'l', 'r', 'b']
    for choice in choices:
        print(f"you inputted {choice}")
        if choice in layer0:
            orient(masterPyraminx, layer0.index(choice))
            moveHorizontal(masterPyraminx, direction, 0)
            # print("in layer 0")
        elif choice in layer1:
            orient(masterPyraminx, layer1.index(choice))
            moveHorizontal(masterPyraminx, direction, 1)
            # print("in layer 1")
        elif choice in layer2:
            orient(masterPyraminx, layer2.index(choice))
            moveHorizontal(masterPyraminx, direction, 2)
            # print("in layer 2")
        elif choice.capitalize() == 'Q':
            print("Goodbye!")
            exit()
        else:
            print(
                "make a choice from the list 'U','L','R','B','Uw', 'Lw', 'Rw', 'Bw','u','l','r','b'")
            
            pass
    names = ['front', 'right', 'left', 'bottom']
    for i in range(len(masterPyraminx)):
        print(names[i])
        print(str(masterPyraminx[i]).replace(
            '], ', ',\n ').replace('[', '').replace(']]', ''))
    
    return masterPyraminx

def main():
    game = True
    while game == True:
        game = getGameMode()


if __name__ == "__main__":
    main()
