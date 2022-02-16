class DSArray:

    # Declaring
    # Time Complexity to perform Declaring - O(1)
    def __init__(self):
        self.arr = []

    # Add element to list
    # Time Complexity : O(1)
    def add_element(self, elt):
        self.arr.append(elt)

    # Insert at a given index
    # Time Complexity : O(1)
    def add_element_index(self, elt, index):
        if index >= len(self.arr):
            print("[ERROR] Index is greater than length")
            return
        self.arr.insert(index, elt)

    # Traversal : Displaying all the elements of the DS
    # going to the all element one by one
    # Time Complexity : n * O(1) = O(n)
    def traversal(self):
        for elt in self.arr:
            print('{0} '.format(elt), end='')

    # Time Complexity : O(n)
    def search(self, search_elt):
        for elt in self.arr:
            if elt == search_elt:
                print('Element {0} Found !!'.format(search_elt))
                return
        print('Element {0} NOT Found !!'.format(search_elt))

    # Delete and element in the list
    def delete(self, del_elt):
        for i in range(0, len(self.arr)):
            if self.arr[i] == del_elt:
                del self.arr[i]
                print('{0} Deleted'.format(del_elt))
                return

        print('{0} Not Found'.format(del_elt))