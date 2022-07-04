# Build an undirected graph as an adjency list from an an edge list
def buildGraph(edges: list()) -> dict():
    graph = dict()
    
    for edge in edges:
        [ a , b ] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    return graph

# Test data
edges = [ ['i', 'j'], ['k', 'i'], ['m', 'k'], ['k', 'l'], ['o', 'n'] ]

# Demo helper function buildGraph
print(buildGraph(edges))