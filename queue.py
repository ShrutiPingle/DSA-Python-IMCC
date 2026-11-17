class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # 1. Enqueue
    def enqueue(self, data):
        new_node = Node(data)

        if self.rear is None:
            self.front = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

    # 2. Dequeue
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return temp.data

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

    # 4. Reverse Queue Using Stack
    def reverse_queue(self):
        stack = []
        temp = self.front

        while temp:
            stack.append(temp.data)
            temp = temp.next

        self.front = self.rear = None

        while stack:
            self.enqueue(stack.pop())

    # 5. Merge Two Queues
    def merge_queue(self, q2):
        merged = Queue()

        temp = self.front
        while temp:
            merged.enqueue(temp.data)
            temp = temp.next

        temp = q2.front
        while temp:
            merged.enqueue(temp.data)
            temp = temp.next

        return merged

    # 6. Check if Two Queues are Identical
    def is_identical(self, q2):
        temp1 = self.front
        temp2 = q2.front

        while temp1 and temp2:
            if temp1.data != temp2.data:
                return False

            temp1 = temp1.next
            temp2 = temp2.next

        return temp1 is None and temp2 is None


# Driver Code
q1 = Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print("Queue 1:")
q1.display()

# print("Dequeued Element:", q1.dequeue())

# q1.display()

# print("After Reversing Queue:")
# q1.reverse_queue()
# q1.display()

q2 = Queue()
q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(60)

print("Queue 2:")
q2.display()

merged_queue = q1.merge_queue(q2)

print("Merged Queue:")
merged_queue.display()

print("Are Queue1 and Queue2 identical?")
print(q1.is_identical(q2))