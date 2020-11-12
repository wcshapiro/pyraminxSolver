Pyraminx Project 1 part 2
CS 463G

*******************ISSUES **************************************

With this program I am having a difficult time getting anything over 4 random moves to run before my computer begins to run noticably slower and I can no longer run the search.
I have found that when I get "lucky" with simple randomizations I can run it fairly well, but for more complex ones it grinds to a halt after wabout 10-15 minutes. 
In addition to that, I believe I have some weird data for timing due to the lucky or unlucky randomizations. This may be the fault of my heuristic as I have seen it go down long rabbit holes at times. 

*******************IMPORTANT NOTE HOW TO RUN **************************************
In this program I created a virtual environment to handle dependencies with some added libraries to use numpy and randomizer. Both of these can
be installed using "pip", Or it can all be setup using the requirements.txt folder I have using the command:
"pip3 install -r requirements.txt". If there is any difficulty getting the setup to work please email me at wcsh228@uky.edu.





*******************Q1: A DESCRIPTION IN ENGLISH OF MY DATA STRUCTURE: *********************************************************
    My data sturcture is a triple nested list.
    Top layer is the pyraminx as a whole with the faces as indexes.
    second layer are the 4 faces indexed by the rows 0-3. And the third layer is made up of the 4 rows indexed by the elements in them which vary in length.
    This proved difficult for rotating vertically, So I rotate and swap each face to what amounts to a 3d-rotation of the pyraminx as a whole. 
    And once the orientation has changed, I perform a horizontal swap. Horizontal swaps are just swapping rows with the numpy.roll method. right vs left determines clockwise vs counterclockwise


    they are oriented as shown below:
     masterPyraminx = [
        [
                                ['R00'],
                        ['R10', 'R11', 'R12'],
                    ['R20', 'R21', 'R22', 'R23', 'R24'],
            ['R30', 'R31', 'R32', 'R33', 'R34', 'R35', 'R36'], ],  # front

        [
                                ['Y00'],
                        ['Y10', 'Y11', 'Y12'],
                    ['Y20', 'Y21', 'Y22', 'Y23', 'Y24'],
            ['Y30', 'Y31', 'Y32', 'Y33', 'Y34', 'Y35', 'Y36'], ],  # right front corner

        [
                                ['G00'],
                        ['G10', 'G11', 'G12'],
                    ['G20', 'G21', 'G22', 'G23', 'G24'],
            ['G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36'], ],  # left front corner


        [['B00', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06'], # bottom front row
                ['B10', 'B11', 'B12', 'B13', 'B14'],
                        ['B20', 'B21', 'B22'],
                            ['B30'],
                        
                    
              
        ]]

************************************** Q2: Code for the data structures, along with instructions on how to run it; **************************************
    code can be found above in the description as well as the main.py in function getGameMode() 
    "python main.py" to run. From there you can press r to randomize, or m to do manual turns
    from there in the randomizer you type the number of random moves you want to make
    if you make manual movements you have to type in a valid sequence for a move. The manual way only works by rotating to the left
    The different possible moves are found in playgame and move subtriangles. U moves top front, L moves left, R=right, B=back. Uw and others with w all take 
    subtriangles, lowercase moves larger subtriangle down to level 3.

    IMPORTANT NOTE:
        the way I implemented the data structure relies on shifting the orientation for every vertical move to turn it into a horizontal move.
        


An example of the GUI output;
        front
        'R00',
        'R10', 'R11', 'R12',
        'R20', 'R21', 'R22', 'R23', 'R24',
        'R30', 'R31', 'R32', 'R33', 'R34', 'R35', 'R36']]
        right
        'Y00',
        'Y10', 'Y11', 'Y12',
        'Y20', 'Y21', 'Y22', 'Y23', 'Y24',
        'Y30', 'Y31', 'Y32', 'Y33', 'Y34', 'Y35', 'Y36']]
        left
        'G00',
        'G10', 'G11', 'G12',
        'G20', 'G21', 'G22', 'G23', 'G24',
        'G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36']]
        bottom
        'B00', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06',
        'B10', 'B11', 'B12', 'B13', 'B14',
        'B20', 'B21', 'B22',
        'B30'
A description of the randomizer;
    the randomizer has the moveable direction choices auto generated. it forms strings that characterize valid moves.

    It can generate multiple random ones at a time and store them in a list. manual moves get sent back as a list of one element while automatic
    mode with a user specifying the number of moves will return a list of that many random valid move strings.
    it then applies the generated moves in order.

Code for the randomizer, along with instructions on how to run it;
    code for the randomizer can be found in the randomizer function 
    instructions. upon typing the choice "r" for randomizer, you may enter the number of moves. Press enter and it will run the randomizer that many times

Your heuristic, clearly described and justified, including an argument that it is admissible;
    my heuristic is adding the number of edge triangles of the wrong color as compared to the middle divided by the number 3. 
     and rounding up (ceiling function). for example,if the tip is the only thing wrong, it would be 3 faces divided by 3 ceiling which gives h=1.
    same goes for single row movements on all levels as the max edge count on a row is 2, so any row with edges wrong will take at least 1 move to fix. 
    This heuristic is admissible as they are lower bounds for number of moves required for
     solving the problem

A statement of what you learned from this assignment.
    One of the most important things I learned is the necessity of forming a good data structure to handle the data
    that needs to be manipulated. Otherwise it is very difficult/ impossible to create good generalizations to make the code much more concise.
    Shorter code also leaves less room for error. Another thing I learned was how many different ways there are to make heuristics. While there may be 
    more than one right answer, there are also many wrong answers and you have to think of lots of scenarios to try and understand how it will operate
    in action. And you have to test it to make sure it is admissible ( lower bound )