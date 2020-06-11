import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# 1. Queue class using an array as the underlying storage structure

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.insert(0,value)

#     def dequeue(self):
#         if not self.storage:
#             return None
#         else:
#             self.size -= 1
#             return self.storage.pop()
            

# q = Queue()
# q.dequeue()
# print(q.__len__())
# print(q.size)

# 2. Queue class, this time using the linked list implementation

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next_node = next
    
#     def get_value(self):
#         return self.value
    
#     def get_next(self):
#         return self.next_node
    
#     def set_next(self, new_next):
#         self.next_node = new_next

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = None
#         self.head = None
#         self.tail = None
#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.size += 1
#         new_node = Node(value)
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def dequeue(self):
#         if self.head is None:
#             return None
#         value = self.head.get_value()
#         if self.head is self.tail:
#             self.size -= 1
#             self.head = None
#             self.tail = None
#         else:
#             self.size -=1 
#             self.head = self.head.get_next()
#         return value
            
# 3. The data is managed in a slightly different way when implementing queues with linked list. 
# Using an array/list the data set is structured and stored in one variable that you can then call methods on to enqueue and dequeue the values.
# With linked lists the data set is grouped by nodes and an individual node needs to be manipulated to add and remove values from the queue.
# This means that there is a lot more code needed to set up the nodes and test different cases for the linked list.

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next_node = next

#     def get_value(self):
#         return self.value
    
#     def get_next(self):
#         return self.next_node

#     def set_next(self, new_next):
#         self.next_node = new_next

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def add_to_tail(self, data):
#         new_node = Node(data)

#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node 
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def remove_tail(self):
#         if self.tail is None:
#             return None

#         data = self.tail.get_value()
        
#         if self.head is self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             current = self.head
#             while current.get_next() != self.tail:
#                 # print(f'tail:{self.tail.get_value()}')
#                 # print(current.get_value())
#                 current = current.get_next()
#             self.tail = None   
#             self.tail = current
            
#         # print(data) 
#         return data

#     def remove_head(self):
#         if self.head is None:
#             return None
        
#         data = self.head.get_value()

#         if self.head is self.tail:
#             self.head = None
#             self.tail = None
#         else:
#             self.head = self.head.get_next()
        
#         return data
    
#     def contains(self, data):
#         if not self.head:
#             return False
        
#         current = self.head

#         while current is not None:
#             if current.get_value() == data:
#                 return True
#             current = current.get_next()
        
#         return False

#     def get_max(self):
#         if self.head is None:
#             return None

#         max_so_far = self.head.get_value()

#         current = self.head.get_next()

#         while current is not None:
#             if current is not None:
#                 if current.get_value() > max_so_far:
#                     max_so_far = current.get_value()

#                 current = current.get_next()
#         return max_so_far

# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()

#     def __len__(self):
#         return self.size

#     def enqueue(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def dequeue(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_head()
#         return None

# dll queue

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)
    
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()
        return None

            
    