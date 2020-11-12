import main
import math
import copy
from functools import reduce


class Node():
    def __init__(self, parent=None, position=None): #creates node instance and sets defaults to 0. g will always be zero because we are not using it but I thought I'd include it anyway.
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = parent
        self.position = position

    def __eq__(self, other): # gets invoked when comparing the objects. Works by reducing each face to see if the color on every face is the same
        testPyraminx = self.position
        complete = True
        for face in testPyraminx:
            comparator = face[0][0][0] # gets the split string, ex. R00 returns R and then it checks all elements on that face to make sure they have R, repeats for all faces
            for row in face:
                for element in row:
                    if element[0] == comparator:
                        pass
                    else:
                        complete = False
        return complete


def astar(maze, start, end,k):
    nodesExpanded = 0 # not counting the first node
    # Creates root node and end node
    rootNode = Node(None, start)
    rootNode.g = rootNode.h = rootNode.f = 0
    endNode = Node(None, end)
    endNode.g = endNode.h = endNode.f = 0

    # creates empty open and closed lists
    open_list = []
    closed_list = []

    # put the beginning node in the open list. 
    open_list.append(rootNode)

    # while the list is not empty
    while len(open_list) > 0:

        # Get node from the front of list
        current_node = open_list[0]
        current_index = 0
        for index, value in enumerate(open_list):
            if value.f < current_node.f: # tests heuristic value against current value so far and puts lowest (best) value at front.
                current_node = value
                current_index = index

        # Take best node off open and add to close
        open_list.pop(current_index)
        closed_list.append(current_node)

        # test to see if we found the goal state. sends to the __eq__ function in class
        if current_node == endNode:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            print(f"nodes expanded = {nodesExpanded}")
            return path[::-1] # returns path

        # Create expansions
        children = []
        counter = 0
        temp = copy.deepcopy(current_node.position) # create copy that can be tested on without changing the current node
        for new_position in ['U', 'L', 'R', 'B', 'Uw', 'Lw', 'Rw', 'Bw', 'u', 'l', 'r', 'b']: # possible moves to test on
            move = [new_position] #needs to be entered as a list element 
            pyraminxCopy = copy.deepcopy(temp)
            counter = counter+1
            node_position = (main.playGame(move,copy.deepcopy(pyraminxCopy),1)) #perform test move and returns pyraminx            
            new_node = Node(current_node, node_position) #creates a node from tested move
            nodesExpanded = nodesExpanded+1
            children.append(new_node) #add to list of expanded for this cycle


        for child in children: # test the children for heuristic and goal against past attempts

            # check to see if child is in closed list
            for closed_child in closed_list: #this works by comparing the unordered set to allow for 3d rotations to be compared directly despite different orientations
                matches = 0
                setOfChild = {
                '0':set(reduce(lambda x,y: x+y,child.position[0])),
                '1':set(reduce(lambda x,y: x+y,child.position[1])),
                '2':set(reduce(lambda x,y: x+y,child.position[2])),
                '3':set(reduce(lambda x,y: x+y,child.position[3]))}
                setOfClosedList = {
                '0':set(reduce(lambda x,y: x+y,closed_child.position[0])),
                '1':set(reduce(lambda x,y: x+y,closed_child.position[1])),
                '2':set(reduce(lambda x,y: x+y,closed_child.position[2])),
                '3':set(reduce(lambda x,y: x+y,closed_child.position[3]))
                }
                for key in setOfChild:
                    for index in setOfClosedList:
                        if setOfChild[key] == setOfClosedList[index]:
                            matches = matches+1
                if matches == 4:
                    continue

            # give f g and h values
            child.g = 0
            child.h = getHeuristic(child.position)
            child.f = child.g + child.h

            # check to see if child is in open list already
            for open_node in open_list:
                matches = 0
                setOfChild = {
                '0':set(reduce(lambda x,y: x+y,child.position[0])),
                '1':set(reduce(lambda x,y: x+y,child.position[1])),
                '2':set(reduce(lambda x,y: x+y,child.position[2])),
                '3':set(reduce(lambda x,y: x+y,child.position[3]))}
                setOfOpenList = {
                '0':set(reduce(lambda x,y: x+y,open_node.position[0])),
                '1':set(reduce(lambda x,y: x+y,open_node.position[1])),
                '2':set(reduce(lambda x,y: x+y,open_node.position[2])),
                '3':set(reduce(lambda x,y: x+y,open_node.position[3]))}
                for key in setOfChild:
                    for index in setOfOpenList:
                        if setOfChild[key] == setOfOpenList[index]:
                            matches = matches+1
                if matches == 4:
                    continue

            # if child not in closed list or open list already, add to open list
            open_list.append(child)
def getHeuristic(pyraminx):
    #get edges of each face as well as corners
    pyraminxEdges = [
    [pyraminx[0][1][0],pyraminx[0][1][2],pyraminx[0][2][0],pyraminx[0][2][4],pyraminx[0][3][2],pyraminx[0][3][4]],
    [pyraminx[1][1][0],pyraminx[1][1][2],pyraminx[1][2][0],pyraminx[1][2][4],pyraminx[1][3][2],pyraminx[1][3][4]],
    [pyraminx[2][1][0],pyraminx[2][1][2],pyraminx[2][2][0],pyraminx[2][2][4],pyraminx[2][3][2],pyraminx[2][3][4]],
    [pyraminx[3][0][2],pyraminx[3][0][4],pyraminx[3][1][0],pyraminx[3][1][4],pyraminx[3][2][0],pyraminx[3][2][2]]
    ]
    pyraminxCorners = [pyraminx[0][0][0],
pyraminx[1][3][0],
pyraminx[2][3][6],
pyraminx[3][3][0],]
    middleColors = [pyraminx[0][2][2][0],pyraminx[1][2][2][0],pyraminx[2][2][2][0],pyraminx[3][1][2][0]] #gets middles of each face. this is the comparator to see if the edges are "wrong"
    i = 0
    outOfPlaceEdges = 0
    for edge in pyraminxEdges:
        for index,value in enumerate(edge):
            if edge[index][0] != middleColors[i]:
                outOfPlaceEdges = outOfPlaceEdges + 1
        i=i+1
    j=0
    for corner in pyraminxCorners:
        if corner[0] != middleColors[j]:
            outOfPlaceEdges = outOfPlaceEdges + 1
        j=j+1

    heuristic = math.ceil(outOfPlaceEdges/4)

    return heuristic