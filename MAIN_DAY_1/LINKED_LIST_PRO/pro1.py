# Define one coach = node
class Node:
    def __init__(self, data):
        self.data = data      # Passenger in Coach
        self.next = None      # Link to next Coach

# Train = Linked List
class LinkedList:
    def __init__(self):
        self.head = None  # First Coach (head of train)

    def add(self, data):
        new_node = Node(data)
        if not self.head:  # If train is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:   # Go to the last Coach
            temp = temp.next
        temp.next = new_node  # Link new Coach at the end

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Test the train
train = LinkedList()
train.add("Coach A")
train.add("Coach B")
train.add("Coach C")
train.display()
