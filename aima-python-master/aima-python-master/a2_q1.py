import csp
import random

# Tested, Trued

def rand_graph(n, p):
    # creates a dictionary with randomized List based on the % p given
    newDict = {}
    for x in range (0,n):
        newList = []
        for y in range (0,n):
            #individuals cannot be friends with themselves
            if y!=x:
                if random.random() <= p:
                    newList.append(y)
            newList.sort
            newDict.update({x:newList})
    #matching friend lists
    #if a is in b's list, and b is not in a's list, add to list
    for x in range (0,n):
        aList = newDict.pop(x)
        for y in range (0,n):
            if y!=x:
                currentList = newDict.get(y)
                if (x in currentList) and (y not in aList):
                    aList.append(y)
            aList.sort
            newDict.update({x:aList})
    return newDict

# For testing
# print(rand_graph(5,1))
# print(rand_graph(5,0.5))
# print(rand_graph(5,0))