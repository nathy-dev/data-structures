from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if not self.has_space():
      print("No room for {}!".format(value))
      return
    item = Node(value)
    item.set_next_node(self.top_item)
    self.top_item = item
    self.size += 1
    print("Adding {} to the stack!".format(value))
  
  def pop(self):
    if not self.is_empty():
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    print("Nothing to pop")

  def peek(self):
    if not self.is_empty():
      return self.top_item.get_value()
    print("Nothing to see here!")

  def has_space(self):
    return self.limit > self.size

  def is_empty(self):
    return self.size == 0