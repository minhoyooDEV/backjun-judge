class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
 
class LinkedQueue:
    def __init__(self):
        self.front = None
        self.rear = None
 
    def is_empty(self):
        if self.front:
            return False
        return True
 
    def put(self, data):
        cur = self.rear
        if cur:
            next = Node(data, cur)
            next.prev = cur
            
            self.rear.next = next
            self.rear = next
        else:
            next = Node(data)
            self.front = next
            self.rear = next
 
    def get(self):
        cur = self.front
        if cur:

            if cur.next:
                cur.prev = None
                self.front = cur.next
            else:
                self.front = None
                self.rear = None
            return cur.data

        return None
 
    def peek(self):
        if self.front:
            return self.front.data
        return None

 
# Test code
queue = LinkedQueue()
 
print(queue.is_empty())
for i in range(10):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(11):
    print(queue.get(), end=' ')
print()
 
for i in range(20):
    queue.put(i)
print(queue.is_empty())
 
for _ in range(5):
    print(queue.peek(), end=' ')
print()
 
for _ in range(21):
    print(queue.get(), end=' ')
print()
print(queue.is_empty())
 