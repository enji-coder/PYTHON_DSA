class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # insert at end point 
    def insert_end(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    # insert at the begining 
    def insert_begining(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # delete node by value 
    def delete_node(self,key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        

        prev = None
        while temp and temp.data != key:
            prev = temp 
            temp = temp.next 

        if temp is None:
            print(f"{key} not found in list")
            return


        prev.next = temp.next
        temp = None

    def display(self):
        temp = self.head
        if not temp:
            print("List is empty")
            return 
        while temp:
            print(temp.data,end="-> ")
            temp = temp.next
        print("None")


l1 = LinkedList()

l1.insert_end(10)
l1.insert_end(20)
l1.insert_end(30)

l1.display()


l1.insert_begining(5)
l1.display()

l1.delete_node(20)
l1.display()

