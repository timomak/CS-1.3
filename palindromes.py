#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def clean_up_text(text):
    text = text.lower()
    if text == '':
        return text
    else:
        text = text.replace(" ", "").translate(str.maketrans('', '', string.punctuation))
        return text

def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # MY METHOD
    # text = clean_up_text(text) # Remove punctuation and put all low caps
    #
    # # Reverse the text
    # reverse = text[::-1]
    #
    # # print(f"Reversed Text: {reverse}")
    # # Checking if both string are equal or not
    # if (text == reverse):
    # return False


    # KJ's and Connor's METHODs Used as reference.
    # It works perfectly, but it's not able to remove punctuation in the pytest, and so the pytest will fail.

    """
    Method will compare the first letter to the last.
    If they don't match, program will return False.
    If they match, program will continue, will compare 2nd letter and 2nd to last letter.
    If they all matched, the method will return True.

    """
    text = clean_up_text(text) # Remove punctuation and put all low caps
    front_index = 0
    back_index = len(text) - 1 # Minus one because we need the last index


    while back_index > front_index:
        if back_index <= front_index:
            break
        if text[back_index] != text[front_index]:
            return False
        front_index += 1
        back_index -= 1
    return True


def is_palindrome_recursive(text, left=None, right=None):
        text = clean_up_text(text) # Remove punctuation and put all low caps
        if left is not None:
            if left > right:
                return True
            if text[left] != text[right]:
                return False
            return is_palindrome_recursive(text, left + 1, right -1 )
        return is_palindrome_recursive(text, 0, len(text) - 1)


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    print(is_palindrome("No, On!"))
    print(clean_up_text(text="No, On!"))
