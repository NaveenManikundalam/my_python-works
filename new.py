class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traverse(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
Kid1 = Node("Max")
Kid2 = Node("Jenny")

family.head.next = wife
wife.next = Kid1
Kid1.next = Kid2

# family.traverse()
family.insert_new_header("Dave")
family.traverse()
 