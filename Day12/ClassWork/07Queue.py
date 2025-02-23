import queue
# print(dir(queue.Queue))

q=queue.Queue()
q.put(10)
q.put(20)
q.put(30)
q.put(40)
print(q.get())
print(q.empty())

#u can also use dequeue to remove from last and start both side.