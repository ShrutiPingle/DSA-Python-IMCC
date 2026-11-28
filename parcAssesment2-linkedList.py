class product:
  def __init__(self,pid,pname,qty,price):
    self.pid=pid
    self.pname=pname
    self.qty=qty
    self.price=price
    self.next=None

class SuperMart:
  def __init__(self):
    self.head=None
    self.price=[]

  def appendP(self,prod):
    if self.head==None:
      self.head=prod
      self.price.append(prod.price)
      return
    temp=self.head
    while temp.next:
      temp=temp.next
    temp.next=prod
    self.price.append(prod.price)
    
  def search(self,key):
    if not self.head:
      return False
    temp=self.head
    while temp:
      if temp.pid==key:
        return True
      temp=temp.next
    return False

  def update(self,pid1,qty1):
    if not self.head:
      print("Empty list")
      return
    temp=self.head
    while temp:
      if temp.pid==pid1:
        temp.qty=qty1
        print(f"Pid:{temp.pid} quantity:{temp.qty}")
        return
      temp=temp.next

  def del_prod(self,pid1):
    if not self.head:
      print("Empty list, nothing to delete")
      return
    temp=self.head
    prev=None
    while temp and temp.pid!=pid1:
      prev=temp
      temp=temp.next
    if temp:
      prev.next=temp.next
      temp=None

  def display(self):
    if not self.head:
      print("Empty list")
      return
    temp=self.head
    while temp:
      print(f"product id:{temp.pid} | product name:{temp.pname} | quantity:{temp.qty} | price:{temp.price}", end="\n")
      temp=temp.next
      
  def find_highest(self):
    if not self.head:
      print("Empty list")
      return
    temp=self.head
    maxp=max(self.price)
    while temp and temp.price!=maxp:
      temp=temp.next
    if temp:
      print(f"product id:{temp.pid} | product name:{temp.pname} | quantity:{temp.qty} | price:{temp.price}", end="\n")

  def sepc_qty(self,qty1):
    if not self.head:
      print("Empty list")
      return
    temp=self.head
    while temp:
      if temp.qty<qty1:
        print(f"product id:{temp.pid} | product name:{temp.pname} | quantity:{temp.qty} | price:{temp.price}", end="\n")
      temp=temp.next
    
s1=SuperMart()
s1.appendP(product(1,"scale",10,10))
s1.appendP(product(2,"biscuit",100,30))
s1.appendP(product(3,"broom",50,200))
s1.appendP(product(4,"lipstick",15,150))
s1.appendP(product(5,"hairtie",300,12))

s1.display()

res=s1.search(3)
if res:
  print("\nproduct found")
else:
  print("\nproduct not found")

s1.update(2,110)

s1.del_prod(5)
print("\nAfter Deletion:")
s1.display()

print("\nproduct with highest Price:")
s1.find_highest()

print("\nproduct with less than specified qty:")
s1.sepc_qty(20)