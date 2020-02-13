import a2_q2

# takes friend dictionary and initalizes CSP
variables = friendList.key() #not needed
domKeys = (variables)
domItems = variables
domains = dict.fromkeys(domKeys, domItems)
neighbors = friendList

def constraints (A, a, B, b):
    # for A,B as individual:team, then check to see if a:b is ok
    #assuming B is already assigned to A, can we assume b is assigned to a?
    for A != B:
        if a==b:
            return False
        else:
            return True
    
# for testing purposes
print("variables: ", variables)
print("domains: ", domains)
print ("neighbours: ", neighbors)







# def exactSolver(graph):
#     # graph represents a good list of friends and bad list for teammates
#     numPeople = len(graph)
#     popularity = {}
#     # get the # of good values
#     for i in graph:
#         popular = len(graph.get(i))
#         popularity.update(i,popular)
        
#     # assign most popular individuals first?