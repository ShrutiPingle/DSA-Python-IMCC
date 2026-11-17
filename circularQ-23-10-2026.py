class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Circularqueue:
  def __init__(self):
    self.front= self.rear =None

  def enqueue(self,newNode):
    if self.rear:
      self.rear.next=newNode
      self.rear=newNode
    else:
      self.front=self.rear=newNode
    self.rear.next=self.front # makes it circular

  def deq(self):
    if self.front:
      temp=self.front
      if self.front==self.rear:
        self.front=self.rear=None
        print("Now Queue is empty")
      else:
        self.front=self.front.next
        self.rear.next=self.front
    else:
      print("Circular queue is empty")

  def print(self):
    if self.front==None:
      print("Queue is empty")
      return
    temp=self.front
    while True:
      print(temp.data,end="<-")
      temp=temp.next
      if temp==self.front:
        break
    print(f"({temp.data})self.front")

cq=Circularqueue()
cq.enqueue(Node(10))
cq.enqueue(Node(20))
cq.enqueue(Node(30))
cq.enqueue(Node(40))
cq.print()

cq.deq()
cq.print()
cq.deq()
cq.print()
cq.deq()
cq.print()
cq.deq()
cq.print()