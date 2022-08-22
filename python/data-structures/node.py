class Node:
  """ Basic generic building block for a data structure.

  Attributes:
    value: Undefined type as it is meant to be generic
    link_node: A reference to a Node object
  """
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

### DEMO Ring Structure ###
node_1 = Node("test data")
node_2 = Node(3)
node_1.link_node = node_2
node_3 = Node(6)
node_2.link_node = node_3
node_4 = Node("traversal about to loop", node_1)
node_3.link_node = node_4

iterations_count = 0
current_node = node_1
while type(current_node.link_node) != None and iterations_count < 10:
    iterations_count += 1
    print("Iteration: ", iterations_count)
    print(current_node.value)
    next_node = current_node.link_node
    current_node = next_node

