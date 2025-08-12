""" 
TASK ::: 1 Create a linked list and reverse it.

Input:  10 -> 20 -> 30 -> None  
Output: 30 -> 20 -> 10 -> None


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

    # Reverse linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # store next
            current.next = prev       # reverse link
            prev = current            # move prev forward
            current = next_node       # move current forward
        self.head = prev

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
ll.add(30)

print("Original List:")
ll.display()

ll.reverse()

print("Reversed List:")
ll.display()
