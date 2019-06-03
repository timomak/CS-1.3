#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

int_to_string = string.digits + string.ascii_lowercase

str_to_int = {string: index for index, string in enumerate(int_to_string)}

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Thank you Connor https://github.com/Connor-Cahill/CS-1.3-Core-Data-Structures/blob/master/Lessons/source/bases.py

    dec_sum = 0
    # i = index and v = value
    for i, v in enumerate(reversed(digits)):
        # str_to_int[v] will return the string (v) as an int.
        # This formula will convert any single string item to its base 10 counnterpart.
        dec_sum += ( base ** i ) * str_to_int[v]
    return dec_sum

# New Code
def encode(number, base):
    '''
    GIVEN NUMBER (BASE10) -> DIGITS IN GIVEN BASE
    '''
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    num = number
    output = ""
    while num > 0:
        remainder = num % base
        # VALUE BY INDEX
        output += string.printable[remainder]
        # ROUNDED DIVISION
        num = num // base
    return output[::-1]

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        # print(result)
        # return result

        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
    # print(25 // 20)
    # encode(14, 14)
    # decode("J", 20)
