#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        # Node counter initialized to zero
        node_count = 0
        # Start at the head node
        node = self.head
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:
            # Count one for this node
            node_count += 1
            # Skip to the next node
            node = node.next
        # Now node_count contains the number of nodes
        return node_count

    def get_at_index(self, index):
        """Return the item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index < self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node at the given index and return its data

        # Checking if the list has any items.
        if self.size > 0:

            # Setting the head to be the first node to search
            node = self.head
            counter = 0

            # Loop until the counter is the index and return the item at that index.
            while counter <= index: # Big O(n) Notation
                if counter == index:
                    return node.data
                else:
                    # if the current node is not at the index, check if the next one is.
                    if node.next != None:
                        node = node.next
                        counter += 1
                    else:
                        raise ValueError('List index out of range: {}'.format(index))
        else:
            raise ValueError('The list is empty')


    def insert_at_index(self, index, item):
        """Insert the given item at the given index in this linked list, or
        raise ValueError if the given index is out of range of the list size.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # Check if the given index is out of range and if so raise an error
        if not (0 <= index <= self.size):
            raise ValueError('List index out of range: {}'.format(index))
        # TODO: Find the node before the given index and insert item after it


        if index == self.size:
            self.append(item)
            return

        if index == 0:
            self.prepend(item)
            return

        # Check if the list has items
        if self.size > 0:
            # Save the current node and the one before that
            node_at_index = self.head
            node_before_index = Node("")
            # Loop until you reach the current index.
            counter = 0
            while counter <= index: # Big O(n)
                # Replace the .next on the node before.
                if counter == index:
                    new_node = Node(data=item)
                    new_node.next = node_at_index
                    node_before_index.next = new_node
                    self.size += 1
                    # print("You have successfully inserted {} after {} at index {}".format(node_at_index, node_before_index, counter))
                    counter += 1
                else:
                    # Set your new node.next to the one at the current index.
                    node_before_index = node_at_index
                    if node_at_index.next != None:
                        node_at_index = node_at_index.next
                        counter += 1
                    else:
                        # check if the last item is the item we're looking for.
                        if counter == index:
                            new_node = Node(data=item)
                            # No need
                            # new_node.next = node_at_index
                            node_before_index.next = new_node
                            # print("You have successfully inserted {} after {} at index {}".format(node_at_index, node_before_index, counter))
                            return
                        else:
                            raise ValueError('List index out of range: {}'.format(index))


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        self.size += 1
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign head to new node
            self.head = new_node
        else:
            # Otherwise insert new node after tail
            self.tail.next = new_node
        # Update tail to new node regardless
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Best and worst case running time: ??? under what conditions? [TODO]"""
        self.size += 1
        # Create a new node to hold the given item
        new_node = Node(item)
        # Check if this linked list is empty
        if self.is_empty():
            # Assign tail to new node
            self.tail = new_node
        else:
            # Otherwise insert new node before head
            new_node.next = self.head
        # Update head to new node regardless
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: Omega(1) if item is near the head of the list.
        Worst case running time: O(n) if item is near the tail of the list or
        not present and we need to loop through all n nodes in the list."""
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Up to n iterations if we don't exit early
            # Check if this node's data satisfies the given quality function
            if quality(node.data):  # Constant time to call quality function
                # We found data satisfying the quality function, so exit early
                return node.data  # Constant time to return data
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # We never found data satisfying quality, but have to return something
        return None  # Constant time to return None

    def replace(self, old_item, new_item):
        """Replace the given old_item in this linked list with given new_item
        using the same node, or raise ValueError if old_item is not found.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        # TODO: Find the node containing the given old_item and replace its
        # data with new_item, without creating a new node object

        # Check if the list has items.
        if self.size > 0:
            # Base nodes
            node = self.head
            # If the list does have items
            found = False
            # while loop until found == True
            while found == False:
                # Loop through nexts until the data matches
                if old_item == node.data:
                    # Replace the node.data with the new data.
                    node.data = new_item
                    found = True
                # Else iterate
                else:
                    node = node.next
                    if node.next == None:
                        if old_item == node.data:
                            # Replace the node.data with the new data.
                            node.data = new_item
                            found = True
                        # Else iterate
                        else:
                            raise ValueError("Item not in list")

        # Else raise error
        else:
            raise ValueError('List is empty')
    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: ??? under what conditions? [TODO]
        Worst case running time: ??? under what conditions? [TODO]"""
        self.size -= 1
        # Start at the head node
        node = self.head
        # Keep track of the node before the one containing the given item
        previous = None
        # Create a flag to track if we have found the given item
        found = False
        # Loop until we have found the given item or the node is None
        while not found and node is not None:
            # Check if the node's data matches the given item
            if node.data == item:
                # We found data matching the given item, so update found flag
                found = True
            else:
                # Skip to the next node
                previous = node
                node = node.next
        # Check if we found the given item or we never did and reached the tail
        if found:
            # Check if we found a node in the middle of this linked list
            if node is not self.head and node is not self.tail:
                # Update the previous node to skip around the found node
                previous.next = node.next
                # Unlink the found node from its next node
                node.next = None
            # Check if we found a node at the head
            if node is self.head:
                # Update head to the next node
                self.head = node.next
                # Unlink the found node from the next node
                node.next = None
            # Check if we found a node at the tail
            if node is self.tail:
                # Check if there is a node before the found node
                if previous is not None:
                    # Unlink the previous node from the found node
                    previous.next = None
                # Update tail to the previous node regardless
                self.tail = previous
        else:
            # Otherwise raise an error to tell the user that delete has failed
            raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    ll = LinkedList(['A', 'B', 'C'])
    print(ll)

    # print('Appending items:')
    # ll.append('A')
    # print(ll)
    # ll.append('B')
    # print(ll)
    # ll.append('C')
    # print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    # print('Getting items by index:')
    # for index in range(ll.size):
    #     item = ll.get_at_index(index)
    #     print('get_at_index({}): {!r}'.format(index, item))
    #
    # print("Adding Z before C")
    # ll.insert_at_index(index=2, item="Z")
    # print("insert_at_index({},{})".format(2, "Z"))

    # print('Deleting items:')
    #
    # print("\nDeleting B")
    # ll.delete('B')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))
    #
    # print("\nDeleting C")
    # ll.delete('C')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))
    #
    # print("\nDeleting A")
    # ll.delete('A')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))
    # print('length: {}'.format(ll.length()))

    # print("Looking for node at index 0")
    # ll.get_at_index(index=0)
    #
    # print("Looking for node at index 3")
    # ll.get_at_index(2)
    #
    # ll.replace("C", "Z")
    # print(ll)

    ll.insert_at_index(0, "Z")
    print("\n",ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(4, "T")
    print("\n",ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))

    ll.insert_at_index(4, "X")
    print("\n",ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))
    print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
