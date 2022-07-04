def breadthFirst(graph: dict(), node: str) -> None:
    # Keep track of nodes to traverse in a first in / first out fashion
    queue = [ node ]
    # Keep visting nodes until there are not more in the graph
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        #For every neighbor of this node add it to a list to check
        for neighbor in graph[current]:
            queue.append(neighbor)

# Test data
graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

# Demo breadth first search
breadthFirst(graph, 'a') # Expected output abcdef
