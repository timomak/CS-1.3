def reduct_words(given_array1=[], given_array2=[]):
    """
        Takes 2 arrays.
        Returns an array with the words from the first array, that were not present in the second array.
    """
    output_array = [] # Array that is gonna be returned

    for word in given_array1: # For each item in the first array, loop O(n)
        if word not in set(given_array2): # Check if the current item is present in the second array.
            output_array.append(word) # Append to output array
    return output_array # return the final array after for loop

# Custom test ;)
if reduct_words([1,2,3,4,5,10], [1,2,3,4,5,6,7,8,9,0]) == [10]:
    print("works")
else:
    print("Doesn't work")
