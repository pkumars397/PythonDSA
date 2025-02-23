class QueueNode:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None 
    def enqueue(self,data):
        newNode=QueueNode(data)
        if self.rear is None:
         self.front=self.rear=newNode
         return 
        self.rear.next=newNode
        self.rear=newNode

    def dequeue(self):
        if self.front is None:
            return None
        temp=self.front
        self.front=temp.next
        if self.front is None:
            self.rear=None 
        return temp.data
    
q=Queue()
q.enqueue(10)
q.enqueue(20)
print(q.dequeue())
       