class Node:
  """ Basic generic building block for a data structure.

  Attributes:
    value: Undefined type as it is meant to be generic
    next_node: A reference to a Node object
  """
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  """ A collection of Nodes that are singularly linked with a defined begining Node
  
  Attributes:
    head_node: A referance to a Node that represents the begining of the linked list
  """
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list

  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
        self.head_node = current_node.get_next_node()
        return

    while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
          break
        current_node = next_node
  
  def swap_nodes(input_list, val1, val2):
    node1 = input_list.head_node
    node2 = input_list.head_node
    node1_prev = None
    node2_prev = None
  
    #Update pointers to previous node
    while node1 is not None:
      if node1.get_value() == val1:
        break
      node1_prev = node1
      node1 = node1.get_next_node()
    
    while node2 is not None:
      if node2.get_value() == val2:
        break
      node2_prev = node2
      node2 = node2.get_next_node()

    if node1_prev is None:
      input_list.head_node = node2
    else:
      node1_prev.set_next_node(node2)
    
    if node2_prev is None:
      input_list.head_node = node1
    else:
      node2_prev.set_next_node(node1)
    
    #Update pointers to next node  
    temp = node1.get_next_node()
    node1.set_next_node(node2.get_next_node())
    node2.set_next_node(temp)


### DEMO ###
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.remove_node(70)
print(ll.stringify_list())