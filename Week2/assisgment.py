class Node:
    def __init__(self, data):
        self.data = data
        self.next = None








class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        if not self.head:
            print("The list is empty.")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("Cannot delete from an empty list.")

        if n <= 0:
            raise IndexError("Index should be a positive integer starting from 1.")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        count = 1
        prev = None

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError("Index out of range.")

        prev.next = current.next
 ## test

if __name__ == "__main__":
    ll = LinkedList()

    # Add some nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)

    print("Initial list:")
    ll.print_list()

    # Delete 2nd node
    try:
        ll.delete_nth_node(2)
        print("\nList after deleting 2nd node:")
        ll.print_list()
    except Exception as e:
        print("Error:", e)

    # Attempt to delete an out-of-range node
    try:
        ll.delete_nth_node(10)
    except Exception as e:
        print("\nError:", e)

    # Delete all nodes one by one
    try:
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        ll.delete_nth_node(1)
        print("\nList after deleting all nodes:")
        ll.print_list()
        # Try deleting from empty list
        ll.delete_nth_node(1)
    except Exception as e:
        print("\nError:", e)
