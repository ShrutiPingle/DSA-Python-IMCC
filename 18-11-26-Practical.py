class node:
    def __init__(self, pro_id, pro_name, priority):
        self.pro_id=pro_id
        self.pro_name=pro_name
        self.priority=priority
        self.next=None


class priority_queue:
    def __init__(self):
        self.front=None

    # 1.Add Process: Insert a process with Process ID, Process Name and Priority (enqueue)
    def enqueue (self, pro_id, pro_name, priority):
        new_node=node(pro_id, pro_name, priority)
        if self.front is None or priority<self.front.priority:
            new_node.next=self.front
            self.front=new_node
        else:
            temp=self.front
            while temp.next is not None and temp.next.priority<=priority:
                temp=temp.next
            new_node.next=temp.next
            temp.next=new_node
        #print("process added successfully")

    # 2.Execute Process: Remove the process with the highest priority (dequeue) 
    def dequeue(self):
        if self.front is None:
            print("no process available")
            return
        temp=self.front
        self.front=self.front.next
        print("executed process:")
        print("process id :", temp.pro_id)
        print("process name :", temp.pro_name)
        print("priority :", temp.priority)

    # 3.View Next Process: Display the next process to be executed (display_next)
    def display_next(self):
        if self.front is None:
            print("no process available")
            return
        print("next process to execute:")
        print("process id :", self.front.pro_id)
        print("process name :", self.front.pro_name)
        print("priority :", self.front.priority)

    # 4.Display Processes: Display all pending processes in priority order (display_all) 
    def display_all(self):
        if self.front is None:
            print("queue is empty")
            return
        temp=self.front
        print("\npending processes:")
        while temp:
            print(
                "id:",
                temp.pro_id,
                ", name:",
                temp.pro_name,
                ", priority:",
                temp.priority,
            )
            temp=temp.next

    # 5.Count Processes: Display the total number of pending processes (count)
    def count(self):
        cnt=0
        temp=self.front
        while temp:
            cnt+=1
            temp=temp.next
        print("total pending processes =", cnt)

pq = priority_queue()
pq.enqueue(101, "system", 1)
pq.enqueue(102, "notepad", 2)
pq.enqueue(103, "music player", 3)
pq.enqueue(104, "video player", 4)
# pq.display_all()

# print()
# pq.count()

# print()
pq.dequeue()
# pq.display_all()

# print()
# pq.display_next()

# print()
# pq.display_all()

print()
pq.count()