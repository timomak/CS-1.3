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
        dec_sum += (base**i) * str_to_int[v]
    return dec_sum

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'numberstr_to_int is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)

    # Thank you Connor https://github.com/Connor-Cahill/CS-1.3-Core-Data-Structures/blob/master/Lessons/source/bases.py

    # number to be returned
    new_base = ''
    # find largest whole number log smaller than number
    if number > 0:
        lg_power = math.floor(math.log(number, base))
    else:
        return '0'
    lg_power = int(lg_power)
    # looping backwards (-1 for 3rd arg) including 0 (-1 for 2nd arg)
    for i in range(lg_power, -1, -1):
        # check if base to power of temp_num less than number
        if base**i <= number:
            # create number to add to return val
            temp_num = number // (base**i)
            # sutbract temp number from number
            number -= temp_num * (base**i)
            new_base += int_to_string[temp_num]
        else:
            # add 0 to output string
            new_base += '0'
    return new_base


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
