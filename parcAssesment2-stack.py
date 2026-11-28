class node:
  def __init__(self,tickid):
    self.tickid=tickid
    self.next=None

class booking:
  def __init__(self):
    self.top=None
    self.cnt=0
  
  def push(self,new_node):
    new_node.next=self.top
    self.top=new_node
    self.cnt+=1

  def display(self):
    temp=self.top
    while temp:
      print(temp.tickid,end="->")
      temp=temp.next
    print()

  def pop(self):
    if self.top is None:
            print("\nStack Underflow")
            return 
    temp=self.top
    self.top=self.top.next
    print("\ndeleted ticket id:",temp.tickid)
    self.cnt-=1
    temp=None
  
  def search(self,key):
    temp=self.top
    while temp and temp.tickid!=key:
      temp=temp.next
    if temp:
      print("ticket found",temp.tickid)
    else:
      print("Ticket not found")

b1=booking()
b1.push(node(10))
b1.push(node(20))
b1.push(node(30))
b1.push(node(40))
b1.push(node(50))

b1.display()

b1.pop()

b1.search(30)

print(f"total tickets in stack: {b1.cnt}")