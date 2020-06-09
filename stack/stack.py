import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# 1. Implement the Stack class using an array as the underlying storage structure
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         return self.storage.append(value)

#     def pop(self):
#         if not self.storage:
#             return None
#         else:
#             return self.storage.pop()

# 2. Re-implement the Stack class, this time using the linked list implementation
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

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = None
#         self.head = None
#         self.tail = None
#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         new_node = Node(value)
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.set_next(new_node)
#             self.tail = new_node

#     def pop(self):
#         if self.tail is None:
#             return None
#         value = self.tail.get_value()
#         if self.head is self.tail:
#             self.size -= 1
#             self.head = None
#             self.tail = None
#         else:
#             self.size -=1 
#             current = self.head
#             while current.get_next() != self.tail:
#                 current = current.get_next()
#             self.tail = current
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

# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = LinkedList()
#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.storage.add_to_tail(value)
#         self.size += 1

#     def pop(self):
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.remove_tail() 
#         return None
# s = Stack()

# s.push(100)
# s.push(101)
# s.push(105)
# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.size)

# stack with dll
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head() 
        return None
