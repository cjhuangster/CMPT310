from csp import*
from a2_q1 import*
from a2_q2 import*



# class Icebreaker(CSP):
friendList = a2_q1.rand_graph(100,0.2)
# takes friend dictionary and initalizes CSP
ibvariables = friendList.keys() #not needed
domKeys = ibvariables
domItems = ibvariables
ibdomains = dict.fromkeys(domKeys, domItems)
ibneighbors = friendList
        
def constraints (A, a, B, b):
    # for A,B as individual:team, then check to see if a:b is ok
    #assuming B is already assigned to A, can we assume b is assigned to a?

        #if individual A, B are neighbours (constrained not to be on same team), and a, b are different teams...
        if a==b:
            return False
        else:
            return True
            
    # def __init__(self, variables, domains, neighbors, constraints): 
    #     self.variables = variables
    #     self.domains = domains
    #     self.neighbors = neighbors 
    #     self.constraints = constraints  
    #     self.curr_domains = None
    #     self.nassigns = 0
    
    
Icebreaker = CSP(ibvariables, ibdomains, ibneighbors, constraints)

# print("friendList:", friendList )
# print("ibdomains: ", ibdomains)
# make_arc_consistent does not work without calling AC3 for whatever reason
print("AC3: ", AC3(Icebreaker))
# print("min_conflicts: ", min_conflicts(Icebreaker))
# print(backtracking_search(Icebreaker))
# for i in domKeys:
#     print(MapColoringCSP(i, ibneighbors))
newDomains = {}
for i in ibdomains:
    for j in ibdomains:
            # print("i, j, possible team for i:", i, " ", j, "       ", make_arc_consistent(i,j,Icebreaker))
            newItem = make_arc_consistent(i,j,Icebreaker)
            newDomains.update({i:newItem})
            
print("newDomains: ", newDomains)
print("check_teams: ", check_teams(friendList, newDomains))




# def exactSolver(graph):
#     # graph represents a good list of friends and bad list for teammates
#     numPeople = len(graph)
#     popularity = {}
#     # get the # of good values
#     for i in graph:
#         popular = len(graph.get(i))
#         popularity.update(i,popular)
        
#     # assign most popular individuals first?

# # for testing purposes
# print("friendList: ", friendList)
# print("variables: ", variables)
# print("domains: ", domains)
# print ("neighbours: ", neighbors)