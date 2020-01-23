# a1.py

from search import *
import random

#Question 1
def make_rand_8puzzle ():
    availableNums = [0,1,2,3,4,5,6,7,8]
    initLst = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
    for x in range (0,8):
        initLst[x] = random.choice(availableNums)
        availableNums.remove(x)
         
    new8Puzzle = search.EightPuzzle(initLst)
    
    while not new8Puzzle.check_solvability():
        availableNums = [0,1,2,3,4,5,6,7,8]
        # initLst = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        initLst = [none]*9
        for x in range (0,8):
            initLst[x] = random.choice(availableNums)
            availableNums.remove(x)
        new8Puzzle = search.EightPuzzle(initLst)
    return new8Puzzle

def display (state):
    for x in range (0,8):
        if state[x]==0:
            state[x]="*"
    for x in range (0,2):
        print(state[x], state[x+1], state[x+2])
    

display(make_rand_8puzzle)
    
#Question 2