"""
    O(log(n)) time complexity
    O(n) space complexity 
"""

class BinaryNode:
    """
        An object that can hold two other same type object values and an integer value

    """
    def __init__(self, value:int=None) -> None:
        self.left_node = None
        self.right_node = None

        self.value = value
    
    def insert(self,value:int) -> None:
        """
            Add a neighbor to this node. Nodes with < data are placed left, > placed right
            on a collision replace this nodes data with the new value
        """
        if not self.value:
            self.val = value
            return
        
        if self.value == value:
            return
        
        if value < self.value:
            if self.left_node:
                self.left_node.insert(value)
            self.left_node = BinaryNode(value)
        
        if value > self.value:
            if self.right_node:
                self.right_node.insert(value)
            self.right_node = BinaryNode(value)
