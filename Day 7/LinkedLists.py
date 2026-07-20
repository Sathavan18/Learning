# Linked lists are made up of individual objects called nodes. 
# Each node stores two things: value and where the next node is (pointer)
# To access a node, you travers using .next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
'''
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
head = node1
node1.next = node2
node2.next = node3

#Traversing:

current = head
while current:
    print(current.value) 
    current = current.next

def contains(head, target):
    current = head
    while current:
        if current.value == target:
            return True
        current = current.next 
    return False

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
head = node1
node1.next = node2
node2.next = node3
print(contains(head, 20))  # True
print(contains(head, 50))  # False

# Inserting at beginning of linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

head = node1

new_node = Node(5)
new_node.next = head
head = new_node
current = head
while current:
    print(current.value) 
    current = current.next
# Method
def insert_at_beginning(head, value):
    new_node = Node(value)

    new_node.next = head

    return new_node
'''
# Insert at the end
def insert_at_end(head, value):
    new_node = Node(value)
    current = head
    if head == None:
        return new_node
    while current.next:
        current = current.next
    current.next = new_node
    return head