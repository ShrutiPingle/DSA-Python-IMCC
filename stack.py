class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # 1. Push
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    # 2. Pop
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return None

        popped = self.top.data
        self.top = self.top.next
        return popped

    # 3. Display
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

    # 4. Reverse String using Stack
    def reverse_string(self, string):
        temp_stack = Stack()

        for ch in string:
            temp_stack.push(ch)

        reversed_str = ""
        while temp_stack.top:
            reversed_str += temp_stack.pop()

        return reversed_str

    # 5. Reverse Stack using Another Stack
    def reverse_stack(self):
        reversed_stack = Stack()

        temp = self.top
        while temp:
            reversed_stack.push(temp.data)
            temp = temp.next

        return reversed_stack

s = Stack()

s.push(10)
s.push(20)
s.push(30)

# s.display()

# print("Popped Element:", s.pop())

# s.display()

# text = "HELLO"
# print("Original String:", text)
# print("Reversed String:", s.reverse_string(text))

rev_stack = s.reverse_stack()

print("Original Stack:")
s.display()

print("Reversed Stack:")
rev_stack.display()