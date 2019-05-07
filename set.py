#!python

from hashtable import HashTable

class Set:
    def __init__(self, elements=None):
        """Initialize this Set list and append the given items, if any."""
        self.data = HashTable() # Using the hashtable functions

        # Append the given elements
        if elements is not None:
            for element in elements:
                self.add(element)

    def __str__(self):
        """Return a formatted string representation of this Set."""
        items = ['({!r})'.format(item) for item in self.data.keys()]
        return '[{}]'.format(' -> '.join(items))

    def __repre__(self):
        """Return a string representation of this Set."""
        return 'Set({!r})'.format(self.data.keys())

    def length(self):
        """Return the length of this Set using the hashtable function."""
        return self.data.length()

    def size(self):
        "Returns number of buckets in Set."
        return self.data.size

    def contains(self, element):
        """Returns a boolean indicating whether element is in this set"""
        return self.data.contains(element)

    def add(self, element):
        """Adds an element to this set, if not present already"""
        # If element is not present in list
        if self.data.contains(element) == False:
            self.data.set(element, element)


    def remove(self, element):
        """Remove element from this set, if present, or else raise KeyError"""
        if self.data.contains(element) == True:
            self.data.delete(element)
        else:
            raise KeyError("Item doesn't exist in Set.")

    def union(self, other_set):
        """Returns a new set that is the union of this set and other_set"""
        combined = [item for item in self.data.keys()]
        combined.extend(item for item in other_set.data.keys())
        return Set(combined)

    def intersection(self, other_set):
        """Returns a new set that is the intersection of this set and other_set"""
        # Thank you Connor!
        intersection = Set()

        larger = self if self.length() >= other_set.length() else other_set
        smaller = self if self.length() < other_set.length() else other_set

        # O(n)^2
        for element in larger.data.keys():
            if smaller.contains(element):
                intersection.add(element)

        return intersection

    def difference(self, other_set):
        """Returns a new set that is the difference of this set and other_set"""
        difference = Set()

        # O(n)^2
        for element in self.data.keys():
            if other_set.contains(element) == False:
                difference.add(element)

        return difference


    def is_subset(self, other_set):
        """Returns a boolean indicating whether other_set is a subset of this set"""
        if other_set.length() < self.length():
            return False

        for element in self.data.keys():
            if not other_set.contains(element):
                return False
        return True

if __name__ == '__main__':
    test = Set(['A','B'])


    print(test)



    test.add('S')

    print(test)
    # print('set(S): ' + str(test))
    # test.add('A')
    # print('set(A): ' + str(test))
    # test.add('F')
    # print('set(F): ' + str(test))
    # test.add('E')
    # print('set(E): ' + str(test))
    # # print('Set: ' + str(test))
    # print('size: ' + str(test.size) + '\n')
    #
    # print('Checking entries:')
    # print('contains(S): ' + str(test.contains('S')))
    # print('contains(A): ' + str(test.contains('A')))
    # print('contains(F): ' + str(test.contains('F')))
    # print('contains(E): ' + str(test.contains('E')))
    # print('')
    #
    # print('Removing entries:')
    # test.remove('S')
    # print('remove(S): ' + str(test))
    # test.remove('A')
    # print('remove(A): ' + str(test))
    # test.remove('F')
    # print('remove(F): ' + str(test))
    # test.remove('E')
    # print('remove(E): ' + str(test))
    # print('contains(F): ' + str(test.contains('F')))
    # print('size: ' + str(test.size))
