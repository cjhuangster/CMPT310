import csp

def rand_graph(n, p):
    # creates a dictionary with randomized set based on the % p given
    newDict = {}
    for x in range (0,n):
        newSet = []
        for y in range (0,n):
            if y!=x:
                if random.random() <= p:
                    newSet.append(y)
            newDict.update({x:newSet})
            newSet = []
            
            
def match_graph