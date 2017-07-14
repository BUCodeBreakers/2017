
'''
CodeBreakers 2017
Week 1 Project
Conway's Game of Life

Objective: Complete the following missing codes to play the game

'''

from graphics import *
from random import random

#Returns 1 if (x,y) is alive else returns 0
def get_state(x,y):
    return matrix[x,y]

#Kill cell @(x,y)
def kill(x,y):
    matrix[x,y] = 0

#Revive cell @(x,y)
def revive(x,y):
    matrix[x,y] = 1

#Draw grid lines    
def draw_grid_lines():
    for i in range(gmax):
        line = Line(Point(0,i), Point(gmax,i))
        line.draw(win)
        line = Line(Point(i,0), Point(i, gmax))
        line.draw(win)

#Initialize MAX n random alive (x,y) grid positions
def StartGame_random(n):
    draw_grid_lines()
    for _ in range(n):
        x = int (random()*gmax)
        y = int (random()*gmax)
        revive(x,y)
        square = Rectangle(Point(x,y), Point(x+1,y+1))
        square.draw(win)
        square.setFill("black")

#Initislize fixed (x,y) alive positions on grid
def StartGame_fixed(X, Y):
    draw_grid_lines()
    for x,y in zip(X,Y):
        revive(x,y)
        square = Rectangle(Point(x,y), Point(x+1,y+1))
        square.draw(win)
        square.setFill("black")

#Return the number of alive neighbors of the cell @(x,y)
def GetAliveNeighborsCount(x,y):
    startx = max(0, x-1)
    starty = max(0, y-1)
    endx = min(gmax, x+2) #Note end index is inclusive
    endy = min(gmax, y+2)
    count = 0
    for x1 in range(startx, endx):
        for y1 in range(starty, endy):
            alive = get_state(x1,y1)
            count += alive 
    count -= get_state(x,y) 
    count = max(0, count)
    return count       

#Print current grid state
def PrintGrid():
    print ('\n--------------------------------------------------------------------')  
    print ('Grid [Number_of_Alive_Neighbors/Alive_or_Dead]: \n')
    count_matrix = GetAliveNeighborsFull()
    for y in range(gmax-1,-1,-1):
        for x in range(gmax):
            if get_state(x,y)>0:
                print "%d/A\t" % (count_matrix[x,y]) , 
            else:
                print "%d/D\t" % (count_matrix[x,y]) ,  
        print     

#Get a dictionary of alive neighbors. ReturnValue[x,y] gives number of alive neighbors at (x,y)
def GetAliveNeighborsFull():
    count_matrix = dict.fromkeys([(i,j) for i in range(gmax) for j in range(gmax)], 0)
    for x in range(gmax):
        for y in range(gmax):
            count_matrix[x,y] = GetAliveNeighborsCount(x,y)
    return count_matrix

#Run the game.. waits for Right key and then implements the rules and continues waiting for next key
def run():
    #Make squares to draw on
    square = {}
    for x in range(gmax):
        for y in range(gmax):
            square[x,y] = Rectangle(Point(x,y), Point(x+1,y+1))
            square[x,y].draw(win)
    step = 0
    print ('\n\nInitialization complete...')
    message = Text(Point(gmax/2, gmax+2), 'Initialization Complete')
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(20)
    message.draw(win)
    key = win.getKey()
    while(key!='Escape'):
        if (key=='Right'):
            message.setText('Running...')
            implement_game_rules()
            for x in range(gmax):
                for y in range(gmax):
                    alive = get_state(x,y)
                    sq = square[x,y]
                    if (alive>0):
                        sq.setFill("black")
                    else:
                        sq.setFill("white")
            step += 1          
            message.setText('Step: '+str(step))
            PrintGrid()                
            print ('Step: ', step)
        key = win.getKey()    


''' ------------------------------------- Editing begins here ---------------------------------- '''

#Implement the rules
'''
Write code here to implement the rules of the game
Hint: 
    use GetAliveNeighborsFull() to get all the neighbors that are alive at each instant
    
    When alive_neighbors = GetAliveNeighborsFull(), alive_neighbors[x,y] will give you the 
    total number of alive neighbors of the cell in (x,y)

    use kill(x,y) to kill a cell @(x,y)
    
    use revive(x,y) to revive a cell @(x,y)
'''
def implement_game_rules():
    return #nothing to return here :) --> just implement the rules..
    

      

'''Edit code here to select between different grid Initializations'''
gmax = 10 #height/width of the grid -- Bigger the grid => Slower the game :(

def main():
    global gmax
    ''' ---------------- Make Changes here ---------------- '''    
    mode = 'Random' #Available options: (Random, Glider, Exploder, Custom)

    if (mode=='Random'):
        '''Random mode: Starts with n alive cells'''
        n = 20
        StartGame_random(n)

    elif (mode=='Glider'):
        '''Glider Mode'''
        X = [1, 2, 3, 3, 2]
        Y = [gmax-4, gmax-4, gmax-4, gmax-3, gmax-2]
        StartGame_fixed(X, Y)

    elif (mode=='Exploder'):
        '''Exploder Mode'''
        X = [gmax/2, gmax/2-1, gmax/2+1, gmax/2-1, gmax/2, gmax/2+1, gmax/2]
        Y = [gmax/2-2, gmax/2-1, gmax/2-1, gmax/2, gmax/2, gmax/2, gmax/2+1]
        StartGame_fixed(X, Y)

    elif (mode == 'Custom'):
        '''Custom Mode: Make custom X and Y'''
        X = []
        Y = []
        StartGame_fixed(X, Y)  

    else:
        '''Default to random'''  
        StartGame_random(20)     
    ''' ---------------- Change ends here ------------------ '''
    
    PrintGrid()
    run()                

''' ------------------------------------- Editing ENDS here ---------------------------------- '''

win = GraphWin('Game of Life', 300, 350)
win.setCoords(0, 0, gmax, gmax+5)
win.setBackground("white")

matrix = dict.fromkeys([(i,j) for i in range(gmax) for j in range(gmax)], 0)
main()
win.close()     