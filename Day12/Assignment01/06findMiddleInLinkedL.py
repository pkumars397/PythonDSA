class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_begin(self,data):
        new_Node=Node(data)
        new_Node.next=self.head
        self.head=new_Node
    def displaY(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    def middle_ll(self):
        slow=self.head
        fast=self.head
        while slow and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data if slow else None

LL=LinkedList()
LL.insert_begin(10)
LL.insert_begin(20)
LL.insert_begin(20)
LL.displaY()
print(LL.middle_ll())