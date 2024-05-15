
# Task 1: Implement the Node class to represent individual nodes in the linked list.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'<Node|{self.value}>'
    
# Task 2: Implement the SinglyLinkedList class with methods for insertion, deletion, and traversal.

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node

    def get_car(self, get_value):
        node_check = self.head
        while node_check:
            if node_check.value == get_value:
                return node_check
            node_check = node_check.next
        return None


    def deletion(self, remove_value):
        if self.head is None:
            print('No cars here!')
            return
        if self.head.value == remove_value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == remove_value:
                current_node = current_node.next.next
            current_node = current_node.next
        print(f'{remove_value} is not here.')

    def traversal(self):
        print('Linked elements:')
        print('head\n | \n V')
        current = self.head
        while current:
            print(current, end=' -> ')
            current = current.next
        print(None)

# Task 3: Test the implemented functionality by performing various operations on the linked list.

# I'm having trouble with the deletion method. I can only delete the head, but not anything further in the linked list. I can't find the problem with the loop, which appears to be the same as the one in class. 

car_list = SinglyLinkedList()
car_list.push('Subaru Forester')
car_list.push('VolksWagen Jetta')
car_list.push('Subaru Baja')
car_list.push('Ford Mustang')
car_list.push('Ford Taurus')
car_list.traversal()
car_list.deletion('Ford Taurus')
car_list.deletion('Ford Mustang')
car_list.traversal()

