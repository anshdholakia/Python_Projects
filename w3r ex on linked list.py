# Write a Python program to create a singly linked list, append some items and iterate through the list
# class Node:
#     # Singly linked node
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None
#
# class singly_linked_list:
#     def __init__(self):
#         # Create an empty list
#         self.tail = None
#         self.head = None
#         self.count = 0
#     def iterate_item(self):
#         # Iterate the list.
#         current_item = self.tail
#         while current_item:
#             val = current_item.data
#             current_item = current_item.next
#             yield val
#     def append_item(self, data):
#         # Append items on the list
#         node = Node(data)
#         if self.head:
#             self.head.next = node
#             self.head = node
#         else:
#             self.tail = node
#             self.head = node
#         self.count += 1
#
# items = singly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
#
# for val in items.iterate_item():
#     print(val)



# Write a Python program to find the size of a singly linked list.
# class Node:
#
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
# class single_linked_list:
#     def __init__(self):
#         self.left=None
#         self.right=None
#         self.count=0
#
#     def append_item(self,data):
#         node=Node(data)
#         if self.right:
#             self.right.next=node
#             self.right=node
#         else:
#             self.left=node
#             self.right=node
#         self.count+=1
#     def iterate(self):
#         current_item=self.left
#         while current_item:
#             val=current_item.data
#             current_item=current_item.next
#             yield val
# item=single_linked_list()
# item.append_item("PHP")
# item.append_item("Python")
# item.append_item("WordPress")
# item.append_item("Java")
# print("Original list")
# for val in item.iterate():
#     print(val)
# print("Size of item:",item.count)



# Write a Python program to search a specific item in a singly linked list and return true if the item is found otherwise
# return false.
# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
# class single_linked_list:
#     def __init__(self):
#         self.left=None
#         self.right=None
#         self.count=0
#
#     def append_item(self,data):
#         node=Node(data)
#         if self.right:
#             self.right.next=node
#             self.right=node
#         else:
#             self.left=node
#             self.right=node
#         self.count+=1
#     def iterate(self):
#         current_item=self.left
#         while current_item:
#             val=current_item.data
#             current_item=current_item.next
#             yield val
#     def search(self,value):
#        for node in self.iterate():
#            if node==value:
#                return True
#        return False
# item=single_linked_list()
# item.append_item("PHP")
# item.append_item("Python")
# item.append_item("WordPress")
# item.append_item("Java")
# print("Original list")
# for val in item.iterate():
#     print(val)
# print(item.search("Jython"))




# Write a Python program to access a specific item in a singly linked list using index value
# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
# class Linked_lis:
#     def __init__(self):
#         self.left=None
#         self.right=None
#         self.count=0
#     def append(self,data):
#         node=Node(data)
#         if self.right:
#             self.right.next=node
#             self.right=node
#         else:
#             self.left=node
#             self.right=node
#         self.count+=1
#     def iterate(self,index):
#         current_item=self.left
#         count=-1
#         while current_item:
#             val=current_item.data
#             current_item=current_item.next
#             count+=1
#             if(count==index):
#                 return val
# item=Linked_lis()
# item.append("PHP")
# item.append("Python")
# item.append("WordPress")
# item.append("Java")
# print(item.iterate(5))



#  Write a Python program to delete the first item from a singly linked list
# class Node:
#     def __init__(self,data=None):
#         self.data=data
#         self.next=None
# class Linked_lis:
#     def __init__(self):
#         self.left=None
#         self.right=None
#         self.count=0
#     def append(self,data):
#         node=Node(data)
#         if self.right:
#             self.right.next=node
#             self.right=node
#         else:
#             self.left=node
#             self.right=node
#         self.count+=1
#     def delete_item(self, data):
#         # Delete an item from the list
#         current = self.left
#         prev = self.left
#         while current:
#             if current.data == data:
#                 if current == self.left:
#                     self.left = current.next
#                 else:
#                     prev.next = current.next
#                 self.count -= 1
#                 return
#             prev = current
#             current = current.next
# items = Linked_lis()
# items.append('PHP')
# items.append('Python')
# items.append('C#')
# items.append('C++')
# items.append('Java')
#
# items.delete_item('PHP')



# Write a Python program to create a doubly linked list, append some items and iterate through the list (print forward)
# class Node(object):
#     # Singly linked node
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append an item
#         new_item = Node(data, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#         self.count += 1
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.data
#             current = current.next
#             yield item_val
#
#     def print_foward(self):
#         for node in self.iter():
#             print(node)
#
#     def reverse(self):
#         """ Reverse linked list. """
#         current = self.head
#         while current:
#             temp = current.next
#             current.next = current.prev
#             current.prev = temp
#             current = current.prev
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# items.append_item('SQL')
#
# print("Reverse list ")
# items.reverse()
# items.print_foward()



# Write a Python program to create a doubly linked list and print nodes from current position to first node
# class Node(object):
#     # Doubly linked node
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append an item
#         new_item = Node(data, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#
#         self.count += 1
#
#     def print_foward(self):
#         for node in self.iter():
#             print(node)
#
#     def print_backward(self):
#         current = self.tail
#         while current:
#             print(current.data)
#             current = current.prev
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.data
#             current = current.next
#             yield item_val
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
#
# print("Print Items in the Doubly linked backwards:")
# items.print_backward()



# Write a Python program to print a given doubly linked list in reverse order
# class Node(object):
#     # Singly linked node
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append an item
#         new_item = Node(data, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#         self.count += 1
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.data
#             current = current.next
#             yield item_val
#
#     def print_foward(self):
#         for node in self.iter():
#             print(node)
#
#     def reverse(self):
#         """ Reverse linked list. """
#         current = self.head
#         while current:
#             temp = current.next
#             current.next = current.prev
#             current.prev = temp
#             current = current.prev
#         temp = self.head
#         self.head = self.tail
#         self.tail = temp
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# items.append_item('SQL')
#
# print("Reverse list ")
# items.reverse()
# items.print_foward()



# Write a Python program to insert an item in front of a given doubly linked list
# class Node(object):
#     # Singly linked node
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append an item
#         new_item = Node(data, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#         self.count += 1
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.data
#             current = current.next
#             yield item_val
#
#     def print_foward(self):
#         for node in self.iter():
#             print(node)
#
#     def insert_start(self, data):
#         if self.head is not None:
#             new_node = Node(data, None, None)
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#             self.count += 1
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# items.append_item('SQL')
#
# print("Original list:")
# items.print_foward()
# print("\nAppend item in front of the list:")
# items.insert_start("Perl")
# items.print_foward()



# Write a Python program to search a specific item in a given doubly linked list and return true
# if the item is found otherwise return false
# class Node(object):
#     # Singly linked node
#     def __init__(self, data=None, next=None, prev=None):
#         self.data = data
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, data):
#         # Append an item
#         new_item = Node(data, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#         self.count += 1
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.data
#             current = current.next
#             yield item_val
#
#     def search(self,valu):
#         for value in self.iter():
#             if value==valu:
#                 return True
#         return False
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# items.append_item('SQL')
#
#
# print(items.search('PHP'))



# Write a Python program to delete a specific item from a given doubly linked list
# class Node(object):
#     # Singly linked node
#     def __init__(self, value=None, next=None, prev=None):
#         self.value = value
#         self.next = next
#         self.prev = prev
#
#
# class doubly_linked_list(object):
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.count = 0
#
#     def append_item(self, value):
#         # Append an item
#         new_item = Node(value, None, None)
#         if self.head is None:
#             self.head = new_item
#             self.tail = self.head
#         else:
#             new_item.prev = self.tail
#             self.tail.next = new_item
#             self.tail = new_item
#         self.count += 1
#
#     def iter(self):
#         # Iterate the list
#         current = self.head
#         while current:
#             item_val = current.value
#             current = current.next
#             yield item_val
#
#     def print_foward(self):
#         for node in self.iter():
#             print(node)
#
#     def search_item(self, val):
#         for node in self.iter():
#             if val == node:
#                 return True
#         return False
#
#     def delete(self, value):
#         # Delete a specific item
#         current = self.head
#         node_deleted = False
#         if current is None:
#             node_deleted = False
#
#         elif current.value == value:
#             self.head = current.next
#             self.head.prev = None
#             node_deleted = True
#
#         elif self.tail.value == value:
#             self.tail = self.tail.prev
#             self.tail.next = None
#             node_deleted = True
#
#         else:
#             while current:
#                 if current.value == value:
#                     current.prev.next = current.next
#                     current.next.prev = current.prev
#                     node_deleted = True
#                 current = current.next
#
#         if node_deleted:
#             self.count -= 1
#
#
# items = doubly_linked_list()
# items.append_item('PHP')
# items.append_item('Python')
# items.append_item('C#')
# items.append_item('C++')
# items.append_item('Java')
# items.append_item('SQL')
#
# print("Original list:")
# items.print_foward()
#
# items.delete("Java")
# items.delete("Python")
# print("\nList after deleting two items:")
# items.print_foward()
