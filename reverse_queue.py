# reversing quesye with using stack
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # 1. Push
    def push(self, node):
        node.next = self.top
        self.top = node
        print(node.data, "pushed into stack")

    def display(self):
        if self.top is None:
            print("Stack is Empty")
            return

        temp = self.top
        print("Stack Elements:")
        while temp:
            print(temp.data, end="<-")
            temp = temp.next
        print()

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        popped = self.top.data
        self.top = self.top.next
        return popped

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


    def enqueue(self, node):
        if self.rear  is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    # 2. Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        deq_data = temp.data
        temp=None
        return deq_data

    # 3. Display
    def display(self):
        if self.front is None:
            print("Queue is Empty")
            return

        temp = self.front
        print("Queue Elements:")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def is_empty(self):
        return self.front is None

def rev_Q(q1):
    st1=Stack()
    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))
    st1.display()

def rev_S(st):
    q2=Queue()
    while not st.is_empty():
        q2.enqueue(Node(st.pop()))
    q2.display()

# Qq=Queue()
# Qq.enqueue(Node(10))
# Qq.enqueue(Node(20))
# Qq.enqueue(Node(30))
# Qq.enqueue(Node(40))

# rev_Q(Qq)

s = Stack()
s.push(Node(11))
s.push(Node(22))
s.push(Node(33))
s.push(Node(44))

rev_S(s)