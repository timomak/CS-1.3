#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    pass
    if (len(array) - 1) < index:
        return None


    if item == array[index]:
        return index

    else:
        return linear_search_recursive(array, item, index + 1)

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_recursive(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, target):
    # TODO: implement binary search iteratively here
    pass

    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (right + left) // 2
        # print(f"Middle: {middle}")
        item = array[middle]

        if item == target:
            return middle
        if item > target:
            left = middle + 1
        elif item < target:
            right = middle - 1
        if left == right:
            if array[left] == target:
                return left
            return None
    return None
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively heres
    if right == None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    middle = (right + left) // 2
    current = array[middle]

    if current == item:
        return middle
    if current < item:
        left = middle + 1
        return binary_search_recursive(array, item, left, right)
    elif current > item:
        right = middle - 1
        return binary_search_recursive(array, item, left, right)
    return None

    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

# if __name__ == '__main__':
#     import sys
#     args = sys.argv[1:]
#     if len(args) == 1:
#         array = ['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick']
#         item = args[0]
#         result = linear_search(array, item)
#         print(f"Found {item} at index {result} of {array}")
#     else:
#         print("Please Provide a name")
