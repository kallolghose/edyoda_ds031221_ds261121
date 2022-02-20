class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    # Create your queue
    def __init__(self):
        self.head = None
        self.tail = None

    # Inserting a data to the queue
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def is_empty(self):
        return self.head is None

    def dequeue(self):
        if self.is_empty():
            print('[ERROR] : Queue is Empty')
            return
        temp_node = self.head
        self.head = self.head.next
        temp_node.next = None

        # When there is only one Node in Queue
        if self.head is None:
            self.tail = None

        return temp_node.data

    def peek_in_queue(self):
        if self.is_empty():
            print('[ERROR] : Queue is Empty')
            return
        return self.head.data

    def delete_queue(self):
        self.head = None
        self.tail = None

    def display(self):
        curr_node = self.head
        while curr_node is not None:
            print(' {} '.format(curr_node.data), end='->')
            curr_node = curr_node.next

