#!python

def contains(text, pattern):
    """
    Return a boolean indicating whether pattern occurs in text.
    Running time: O(n) because it needs to compare it to each item linearly.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern in text:
        return True
    return False

def find_index(text, pattern):
    """
    Return the starting index of the first occurrence of pattern in text, or None if not found.
    Running time: O(n) because we need to iterate on the string.
    """
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    #
    # TODO: Implement find_index here (iteratively and/or recursively)
    indices = find_all_indexes(text, pattern)
    if len(indices) > 0:
        return indices[0]
    return None


def find_all_indexes(text, pattern):
    """
    Return a list of starting indexes of all occurrences of pattern in text, or an empty list if not found.
    Running time: O(n) because we need to check each char in string.
    """
    #

    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    # Class Implementation
    # https://github.com/lvreynoso/CS1.3-Coursework/blob/master/strings.py
    # time complexity - best case O(n), worse case O(nm)?
    if pattern == '':
        return [position for position, character in enumerate(text)]

    indices = []
    candidates = {}
    delta = len(pattern)
    for position, character in enumerate(text):
        # try to match all the first letters of the pattern
        if character == pattern[0]:
            candidates[position] = 1
        for index, streak in candidates.items():
            if streak != False:
                if index != position and character == pattern[streak]:
                    candidates[index] += 1
                elif index != position and character != pattern[streak]:
                    candidates[index] = False
                if candidates[index] == delta:
                        indices.append(index)
                        candidates[index] = False
    return indices


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))

    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))

    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))



def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")

if __name__ == '__main__':
    main()
