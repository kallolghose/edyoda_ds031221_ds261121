class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("[ERROR] : Stack is empty")
            return
        temp_node = self.top
        self.top = self.top.next
        temp_node.next = None
        return temp_node.data

    def peek(self):
        if self.is_empty():
            print("[ERROR] : Stack is empty")
            return
        return self.top.data

    def delete_stack(self):
        self.top = None

    def display(self):
        current_node = self.top
        while current_node is not None:
            print(" | {} |".format(current_node.data))
            print(" ~~~~~~")
            current_node = current_node.next



