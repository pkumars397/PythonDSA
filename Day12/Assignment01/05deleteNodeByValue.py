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
    def deleteNode(self,value):
        temp=self.head
        if temp and temp.data==value:
            self.head=temp.next
            return 
        while temp and temp.next and temp.next.data!=value:
            temp=temp.next
        if temp and temp.next:
            temp.next=temp.next.next

LL=LinkedList()
LL.insert_begin(10)
LL.insert_begin(20)
LL.displaY()

#delete Node 20
LL.deleteNode(20)
LL.displaY()