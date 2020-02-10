def exactSolver(graph):
    # graph represents a good list of friends and bad list for teammates
    numPeople = len(graph)
    popularity = {}
    # get the # of good values
    for i in graph:
        popular = len(graph.get(i))
        popularity.update(i,popular)
        
    # assign most popular individuals first