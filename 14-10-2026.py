class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CSLL:
    def __init__(self):
        self.head=None
        self.size=0
    
    def append(self, data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            newNode.next=self.head
            self.size+=1
            return
        temp=self.head
        while temp.next!=self.head:
            temp=temp.next
        temp.next=newNode
        newNode.next=self.head
        self.size+=1

    def traverse(self):
        temp=self.head
        while True:
            print(temp.data, end="->")
            temp=temp.next
            if temp==self.head:
              break
        print(temp.data)

    def insert_at(self, val, pos):
        newNode = Node(val)
        if pos==0:
            print("please enter postion from 1st! , hence not inserted")
            return
        if pos == 1:
            if not self.head:
                # Empty list 
                self.head = newNode
                newNode.next = self.head
            else:
                temp = self.head
                while temp.next != self.head:
                    temp = temp.next
                newNode.next = self.head
                self.head = newNode
                temp.next = self.head
            self.size += 1
            return
        #other positions
        temp = self.head
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1
            if temp == self.head:  # looped back → out of range
                print("Position out of range")
                return

        newNode.next = temp.next
        temp.next = newNode
        self.size += 1


    def deleteNode(self,val):
        temp=self.head
        prev=None
        if temp.data==val:
            while temp.next != self.head:
                temp = temp.next
            self.head=self.head.next
            temp.next = self.head
            return
        while temp and temp.data!=val:
            prev=temp
            temp=temp.next
        if temp:
            prev.next=temp.next
            temp=None

Csll=CSLL()
Csll.append(1)
Csll.append(2)
Csll.append(3)
Csll.append(4)
Csll.append(5)

print("Circular Linked List:")
Csll.traverse()

# Csll.insert_at(9,6)
# print("Circular Linked list after insertion: ")
# Csll.traverse()

Csll.deleteNode(1)
print("list after deletion: ")
Csll.traverse()