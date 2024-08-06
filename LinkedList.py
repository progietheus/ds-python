#Linked List
#Python does not have a built-in linked list. Normally, in an interview, you would be given a definition like this.
#Appending to end - O(1)
#Finding an element - O(N)

class LinkedListNode:
# _init__ method in Python is used to initialize objects of a class. It is also called a constructor.
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

#Besides problems that specifically ask for linked lists, it is not common to define and use a linked list. If you need a list with O(1) append you can use the built-in list, and if you want O(1) for both prepend and append you can use the built-in deque.
