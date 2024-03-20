class Queue:
   def __init__(self,size):
      self.size = size
      self.queue = [None] * size
      self.front = 0
      self.rear = -1
      self.count = 0
   def isempty(self):
      return self.count == 0
   def isfull(self):
      return self.count == self.size
   def enqueue(self,item):
      if self.isfull():
         print("Queue is full")
         return
      self.rear = (self.rear+1)%self.size
      self.queue[self.rear] = item
      self.count += 1
   def dequeue(self):
      if self.isempty():
         print("Queue is empty")
         return None
      item = self.queue[self.front]
      self.front = (self.front+1)%self.size
      self.count -= 1
      return item
   def peekitem(self):
      if self.isempty():
         return None
      return self.queue[self.front]
queue = Queue(6)
queue.enqueue(10)
queue.enqueue(14)
queue.enqueue(5)
print("Is queue empty:", queue.isempty())
print('Front of the queue:',queue.peekitem())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Is queue empty", queue.isempty())
      
      
   