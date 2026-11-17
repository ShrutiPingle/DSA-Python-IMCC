class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Linearqueue:
  def __init__(self):
    self.front= self.rear =None

  def enqueue(self,newNode):
    if self.rear:
      self.rear.next=newNode
      self.rear=newNode
    else:
      self.front=self.rear=newNode

  def deq(self):
    if self.rear:
      temp=self.front
      self.front=self.front.next
      if self.front==None:
        self.rear=None
        print("Now Queue is empty")
      temp=None
    else:
      print("linear queue is empty")

  def print(self):
    if not self.front:
      print("Queue is empty")
      return
    temp=self.front
    while temp:
      print(temp.data,end="<-")
      temp=temp.next
    print("None")

lq=Linearqueue()
lq.enqueue(Node(10))
lq.enqueue(Node(20))
lq.enqueue(Node(30))
lq.enqueue(Node(40))

lq.print()

lq.deq()
lq.print()
lq.deq()
lq.print()
lq.deq()
lq.print()
lq.deq()
lq.print()