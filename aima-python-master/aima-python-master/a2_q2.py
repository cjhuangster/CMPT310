import csp
import a2_q1

def check_teams(graph, csp_sol):
#since solution in sets of (individual#:team#)
    teamNums = csp_sol.values()
    for x in teamNums:
        aTeam = []
        for y in csp_sol:
            #provides a list of all team members on a tea
            if csp_sol.get(y) == x:
                aTeam.append(y)
        # check if any teams and any friend lists share pairs
        for i in aTeam:
            aFriendList = graph.get(i)
            for j in aTeam:
                if j in aFriendList:
                    return False
    return True