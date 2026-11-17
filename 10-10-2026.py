class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__(self):
        self.head=None
        self.size=0
    
    def append(self, data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            self.size+=1
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
        self.size+=1

    def traverse(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next
        print("None")

    def insert_at(self, val, pos):
        newNode=Node(val)
        if pos==0:
            newNode.next=self.head
            self.head=newNode
            self.size+=1
            return    
        temp=self.head
        count=0
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
        if temp is None:
            print("position out of range")
            return

        newNode.next = temp.next
        temp.next = newNode
        self.size+=1

    def middle(self):
        prev=self.head
        temp=self.head
        while temp and temp.next:
            prev=prev.next
            temp=temp.next.next
        if prev:
            print("Mid Node is : ",prev.data)
         
    def middle_delete(self):
        if self.head is None:
            print("List is empty")
            return
        if self.size <= 1:
            print("linked List size is", self.size,)
            self.head = None
            return
        mid_index = self.size // 2   # middle position
        temp = self.head
        prev = None
        count = 0
        while temp is not None and count < mid_index:
            prev = temp
            temp = temp.next
            count += 1
        if temp is None:
            print("Position out of range")
            return
        prev.next = temp.next
        print("Deleted middle node with value:", temp.data)
        temp=None

    def del_first_last(self):
        temp=self.head
        if self.size==1:
            print("only one node to delete")
            self.head=None
            return
        temp=self.head
        self.head=temp.next
        temp=None
        temp1=self.head
        while(temp1.next):
            prev=temp1
            temp1=temp1.next
        prev.next=temp1.next
        temp1=None
        
    def deleteNode(self,val):
        temp=self.head
        if temp and temp.data==val:
            self.head=temp.next
            temp=None
        prev=None
        while temp and temp.data!=val:
            prev=temp
            temp=temp.next
        if temp:
            prev.next=temp.next
            temp=None

    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        self.head=prev

    def cal_sum(self):
        temp=self.head
        while temp and temp.next:
            print(temp.data+temp.next.data,end=" ")
            temp=temp.next.next
    
sll=SLL()
sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

print("Linked List:")
sll.traverse()

# sll.insert_at(9,2)
# print("Linked list after insertion: ")
# sll.traverse()

# sll.middle()

# sll.deleteNode(3)
# print("list after deletion: ")
# sll.traverse()

# sll.reverse()
# print( "after reversing: ")
# sll.traverse()

# print("calculating sum of 2 consecutive numbers")
# sll.cal_sum()

# sll.middle_delete()
# print( "after middle delete: ")
# sll.traverse()

sll.del_first_last()
print( "after 1st and last delete: ")
sll.traverse()