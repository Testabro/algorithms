def breadthFirst(graph: dict(), node: str) -> None:
    queue = [ node ]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)

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
