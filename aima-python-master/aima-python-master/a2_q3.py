from csp import* 
from a2_q1 import* 
from a2_q2 import* 
import xlsxwriter
import time

run_q3
def run_q3():
    workbook = xlsxwriter.Workbook('a2_q3.xlsx')
    worksheet = workbook.add_worksheet()
    labels = ["probability", "#teams", "run time", "#assign", "#unassign", "fun fact: team assignments"]
    row = 0
    column = 0
    for item in labels:
        worksheet.write(row,column,item)
        column+=1
        
    def constraints (A, a, B, b):
        # for A,B as individual:team, then check to see if a:b is ok
        #assuming B is already assigned to A, can we assume b is assigned to a?

            #if individual A, B are neighbours (constrained not to be on same team), and a, b are different teams...
            if a==b:
                return False
            else:
                return True

    for x in range (5):
        graphs = [rand_graph(30, 0.1), rand_graph(30, 0.2), rand_graph(30, 0.3),
            rand_graph(30, 0.4), rand_graph(30, 0.5)]
        # friendList = rand_graph(100,0.2)
        for y in range(len(graphs)): 
            startTime = time.time()
            friendList = graphs[y]
            # takes friend dictionary and initalizes CSP
            ibvariables = friendList.keys() #not needed
            domKeys = ibvariables
            domItems = ibvariables
            ibdomains = dict.fromkeys(domKeys, domItems)
            ibneighbors = friendList
            
            Icebreaker = CSP(ibvariables, ibdomains, ibneighbors, constraints)
            AC3(Icebreaker)
            backtracking_search(Icebreaker)
            # print("check_teams backtracking: ", check_teams(friendList, backtracking_search (Icebreaker)))
            # print("backtracking_search: ", (backtracking_search(Icebreaker)))
            teams = (backtracking_search(Icebreaker))
            # print("#team", max(teams.values()))
            # # print("bt size: ", max(backtracking_search(Icebreaker)).values())
            # print("#assigned:", Icebreaker.nassigns)
            # print("#unassigned", Icebreaker.nassigns-len(ibvariables))
            endTime = time.time()
            # print("calculation time: ", endTime - startTime)
            
            teamNum = max(teams.values())
            numAssign = Icebreaker.nassigns
            numUnassign = Icebreaker.nassigns-len(ibvariables)
            calcTime = endTime - startTime
            #  "to be honest I don't even know whats happening here"
            content = [y*0.1+0.1, teamNum, calcTime, numAssign, numUnassign, str(teams)]
            row = x*5+y+1
            column = 0
            for item in content:
                worksheet.write(row,column,item)
                column+=1

    workbook.close()  