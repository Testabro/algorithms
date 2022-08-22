def depthFirstWithRecursion(graph: dict(), node: str, visited=set()):
    print(node)
    for neighbor in graph.get(node):
        #Protect against cycles by marking a node as visited
        if neighbor in visited: continue
        visited.add(neighbor)
        depthFirstWithRecursion(graph, neighbor)

def depthFirstNoRecursion(graph: dict(), rootNode: str) -> None:
    #Create a stack since we are not using recursion to manage the stack
    stack = [ rootNode ]

    while (len(stack) > 0):
        #Get a value to the current stack item and remove it off the top
        current = stack.pop()
        #Print the node that was just removed from the stack
        print(current)

        #Get all the neighbors of the current node and push them onto the stack
        for neighbor in graph[current]:
            stack.append(neighbor)

#Test data
graph = {
    'a': ['b','c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
}

#Demo depth first with no recursion
print("Depth First Algorithm w/o Recursion")
print("Graph:", graph)
depthFirstNoRecursion(graph, 'a') # Expected output of the traversial is acebdf

#Demo depth first with no recursion
print("Depth First Algorithm w/ Recursion")
print("Graph: ", graph)
depthFirstWithRecursion(graph, 'a') # Expected output of the traversial is abdfce <- call stack vs built stack
