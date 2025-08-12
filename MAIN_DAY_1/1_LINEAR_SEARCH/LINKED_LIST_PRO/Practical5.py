# TASK ::: 2 — Remove Duplicate Elements from a Linked List
# Problem Statement:
# Create a linked list and remove all duplicate elements (keeping only the first occurrence).

""" 
Input:  10 -> 20 -> 20 -> 30 -> 10 -> None  
Output: 10 -> 20 -> 30 -> None

"""

# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Add node at end
    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Remove duplicates
    def remove_duplicates(self):
        seen = set()
        current = self.head
        prev = None
        while current:
            if current.data in seen:
                prev.next = current.next  # skip the duplicate
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    # Display list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# ==== Test ====
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(20)
ll.add(30)
ll.add(10)

print("Original List:")
ll.display()

ll.remove_duplicates()

print("List After Removing Duplicates:")
ll.display()
