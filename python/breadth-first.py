def breadthFirst(graph: dict(), node: str) -> None:
    # Cycle guard -> no duplicate entries; will only be used to see if a node has been visted
    visted = set()
    queue = [ node ]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

        for neighbor in graph[current]:
            #Check if this node has been visted already
            if current in visted: continue
             
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
