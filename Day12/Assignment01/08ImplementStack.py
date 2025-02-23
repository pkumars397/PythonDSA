#we can implement stack using list data structure
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    def is_empty(self):
        return len(self.stack)==0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]
s=Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.pop())
print(s.is_empty())
print(s.peek())