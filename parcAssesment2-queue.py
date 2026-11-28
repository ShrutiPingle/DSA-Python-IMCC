class node:
  def __init__(self,pid,pname,priority):
    self.pid=pid
    self.pname=pname
    self.priority=priority
    self.next=None

class Queue:
  def __init__(self):
    self.front=None

  def enqueue(self,new_node):
    if self.front is None or new_node.priority<self.front.priority:
      new_node.next=self.front
      self.front=new_node
      return
    temp=self.front
    while temp.next is not None and temp.next.priority<=new_node.priority:
      temp=temp.next
    new_node.next=temp.next
    temp.next=new_node

  def dequeue(self):
    temp=self.front
    self.front=self.front.next
    print(f"Paitent dequeud : {temp.pname} | id:{temp.pid}\n")
    temp=None

  def display_next(self):
    if self.front is None:
      print("no paitent in queue")
      return
    print(f"\nNext paitent is : {self.front.pname} | id:{self.front.pid}\n")

  def display_all(self):
    temp=self.front
    if self.front is None:
      print("queue is empty")
      return
    while temp:
      print(f"priority:{temp.priority} | paitent name: {temp.pname} | id:{temp.pid}", end="\n")
      temp=temp.next

q1=Queue()
q1.enqueue(node(101,"ashutosh",2))
q1.enqueue(node(102,"kaivalya",1))
q1.enqueue(node(103,"minal",3))
q1.enqueue(node(104,"anna",1))

print("\nAll the paitents in the queue")
q1.display_all()

q1.display_next()

q1.dequeue()

print("All the paitents in the queue")
q1.display_all()