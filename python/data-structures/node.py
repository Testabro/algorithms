class Node:
  """ Basic generic building block for a data structure.

  Attributes:
    value: Undefined type as it is meant to be generic
    link_node: A reference to a Node object
  """
  def __init__(self, value, link_node=None):
      self.value = value
      self.link_node = link_node
      
  def get_value(self):
      return self.value

  def get_link_node(self):
      return self.link_node

  def set_link_node(self, link_node) -> None:
      self.link_node = link_node

### DEMO Ring Structure ###
node_1 = Node("test data")
node_2 = Node(3)
node_1.set_link_node(node_2)
node_3 = Node(6)
node_2.set_link_node(node_3)
node_4 = Node("traversal about to loop", node_1)
node_3.set_link_node(node_4)

iterations_count = 0
current_node = node_1
while type(current_node.link_node) != None and iterations_count < 10:
    iterations_count += 1
    print("Iteration: ", iterations_count)
    print(current_node.get_value())
    next_node = current_node.get_link_node()
    current_node = next_node

