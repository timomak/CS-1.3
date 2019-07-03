# coding: utf-8
#!python

from linkedlist import LinkedList

# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.

        Runtime: O(1) because no shifting
        """
        # TODO: Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        temp = self.list.head
        if temp != None:
            return temp.data
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,

        Runtime: O(1) because head with no shifting.
        """
        # TODO: Remove and return top item, if any
        temp = self.list.head
        if temp != None:
            self.list.delete(temp.data) # O(n)
            return temp.data
        else:
            raise ValueError("Empty list")

# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if self.length() == 0:
            return True
        else:
            return False

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.

        Runtime: O(1) because of no shifting
        """
        # TODO: Insert given item
        self.list.append(item) # end of the list

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.is_empty() == False:
            return self.list[-1]
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,

        Runtime: O(1) because of end of list
        """
        # TODO: Remove and return top item, if any
        if self.is_empty() == False:
            temp = self.list[-1]
            self.list.pop()
            return temp
        else:
            raise ValueError("Empty list")


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
# if __name__ == '__main__':
#     # Stack = LinkedStack()
#     Stack = ArrayStack()
#     #
#     # print("Stack:", Stack)
#     #
#     Stack.push("A")
#     print(Stack)
#
#     list = list()
#
#     list.insert(0, "A")
#
#     print(list[0])
