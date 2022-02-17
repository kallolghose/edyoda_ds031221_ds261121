class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def create(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node
        self.size = self.size + 1

    def is_empty(self):
        return self.head is None

    def insert(self, data, start=False, end=False, location=0):
        if self.is_empty():
            print("[ERROR] List is empty please use create()")
            return
        new_node = Node(data)
        if start:
            new_node.next = self.head
            self.head = new_node
        elif end:
            self.tail.next = new_node
            self.tail = new_node
        else:
            if location == 0 or location == 1 or location >= self.size:
                print("[ERROR] Please enter a proper location")
                return
            # 1. Move from head to location - 1
            # 2. Update the next of New Node
            # 3. Update the next of tempNode (Node 2)
            temp_node = self.head
            for _ in range(1, location-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node

        self.size = self.size + 1

    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print("{}".format(current_node.data), end=" -> ")
            current_node = current_node.next

    def search(self, search_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == search_data:
                print("Value {} Found".format(search_data))
                return
            current_node = current_node.next

        print("Value {} NOT Found".format(search_data))

    def delete(self, start=False, end=False, location=0):
        if not self.is_empty():
            print("[ERROR] : Linked List Is Empty")
            return
        if start:
            self.head = self.head.next
            if self.size == 1:
                self.tail = None
        elif end:
            if self.size == 1:
                self.head = None
                self.tail = None
            temp_node = self.head
            for i in range(0, self.size - 1):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        else:
            if location == 0 or location==1 or location >= self.size:
                print("[ERROR] Please enter a proper location")
                return
            temp_node = self.head
            for i in range(0, location - 1):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next
        self.size = self.size - 1


