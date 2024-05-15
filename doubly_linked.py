
# Task 1: Implement the **Node** class to represent individual nodes in the doubly linked list.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'<Node|{self.value}>'

# Task 2: Implement the **DoublyLinkedList** class with methods for insertion, deletion, and traversal.

class DoubleTrouble:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node
    
    def traverse(self):
        print('Linked List Elements: ')
        print('Head\n | \n V')
        current = self.head
        while current:
            print(current, end=' <--> ')
            current = current.next
        print(None)

    def remove(self, value_to_remove):
        if self.head is None:
            print("Ain't nothing here, dude.")
            return
        if self.head.value == value_to_remove:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return
        current_node = self.head
        while current_node:
            if current_node.value == value_to_remove:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                    return
            current_node = current_node.next
        print(f'{value_to_remove} is not here.')


car_list = DoubleTrouble()
car_list.append('Subaru Forester')
car_list.append('VolksWagen Jetta')
car_list.append('Subaru Baja')
car_list.append('Ford Mustang')
car_list.append('Ford Taurus')
car_list.traverse()
car_list.remove('Ford Taurus')
car_list.remove('Ford Mustang')
car_list.traverse()

