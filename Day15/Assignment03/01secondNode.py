class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newNode
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    def middleNode(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow.data
    
ll=LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.display()
print(ll.middleNode())