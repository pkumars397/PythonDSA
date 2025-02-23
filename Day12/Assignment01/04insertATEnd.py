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

    def insert_end(self,data):
        newNode=Node(data)
        if not self.head:
            self.head=newNode
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
    def displaY(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)

LL=LinkedList()
LL.insert_begin(10)
LL.insert_begin(20)
LL.displaY()
LL.insert_end(30)
LL.displaY()