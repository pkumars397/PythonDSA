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
    def reverseList(self):
        prev=None
        current=self.head
        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        self.head=prev

LL=LinkedList()
LL.insert_begin(10)
LL.insert_begin(20)
LL.displaY()

LL.reverseList()
LL.displaY()