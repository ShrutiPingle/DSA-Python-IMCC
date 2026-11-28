class node:
  def __init__(self,pid,pname,priority):
    self.pid=pid
    self.pname=pname
    self.priority=priority
    self.next=None

class Queue:
  def __init__(self):
    self.front==self.rear=None

  def enqueue(self,new_node):
    if self.front is None or new_node.priority<self.front.priority:
      new_node.next=self.front
      self.front=new_node
      return
    temp=self.front
    while temp.next is not None and temp.priority!<=new_node.priority:
      temp=temp.next
    new_node.next=temp.next
    temp.next=new_node

  def dequeue(self):
    pass

  def display_next(self):
    if self.front is None:
      print("no paitent in queue")
      return
    print(f"Next paitent is :{self.front.pname}")
      