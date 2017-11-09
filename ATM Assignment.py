import time
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def peek(self):
         return self.items[len(self.items)-1]

q=Queue()
q.enqueue('Muchaneta')
q.enqueue('Tarisai')
q.enqueue('Nhamoinesu')
q.enqueue('Takunda')
q.enqueue('Rose')
q.enqueue('Tafira')

start = time.time()
for i in range(6):

     time.sleep(5)
     print( " person on queue", q.dequeue ())
     end = time.time()
     print(end - start)

     for i in range(5):

          time.sleep(8)
          print( " person on queue", q.dequeue ())
          end = time.time()
          print(end - start)


if q.isEmpty():
    for i in range (6):
        s = str(input('Enter Name \n'))
        q.enqueue(s)
