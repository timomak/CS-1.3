#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)
    if base is 2:
        answer = 0
        lenght = len(digits) - 1
        for num in digits:
            num = int(num)
            value = num * (base ** lenght)
            lenght -= 1
            answer += value
        return answer

    # TODO: Decode digits from hexadecimal (base 16)

    # Thanks to KJ for figuring it out!
    elif base is 16:
        answer = 0
        lenght = len(digits) - 1

        for num in digits:
            if num.isalpha():
                num = num.upper()
                if num == "A":
                    num = 10
                elif num == "B":
                    num = 11
                elif num == "C":
                    num = 12
                if num == "D":
                    num = 13
                if num == "E":
                    num = 14
                if num == "F":
                    num = 15
            num = int(num)

            answer += num * (base ** lenght)
            lenght -= 1
        return answer

    # TODO: Decode digits from any base (2 up to 36)

    # Thanks to KJ for figuring it out too!
    elif 2 < base < 36:
        answer = 0
        lenght = len(digits) - 1
        for number in digits:
            if number.isalpha():
                number = number.upper()
                number = string.ascii_uppercase.index(number) + 10
            number = int(number)
            answer += number * (base ** lenght)
            lenght -= 1
        return answer


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    # TODO: Encode number in binary (base 2)
    if base == 2:
        number_array = [number]
        answer = ""

        # Keep the loop until it finished diving it.
        while number > 1:
            number = number // 2
            number_array.append(number)

        # Convert each number in array to one binary number.
        for num in number_array:
            answer = str(num % 2) + answer

        # Return
        return answer

    # TODO: Encode number in hexadecimal (base 16)
    elif base == 16:
        hex = ""
        while number > 0:
            hex_num = number % 16
            number = number // 16
            new_hex_value = hex_num
            if hex_num < 10:
                new_hex_value = hex_num
            elif hex_num == 10:
                new_hex_value = "A"
            elif hex_num == 11:
                new_hex_value = "B"
            elif hex_num == 12:
                new_hex_value = "C"
            elif hex_num == 13:
                new_hex_value = "D"
            elif hex_num == 14:
                new_hex_value = "E"
            elif hex_num == 15:
                new_hex_value = "F"

            hex = str(new_hex_value) + hex

        return hex
    # TODO: Encode number in any base (2 up to 36)
    elif 2 < base < 36:
        answer = ""
        while number > 0:
            value = number % base
            number = number // base
            if value >= 10 and value < base:
                value = string.ascii_uppercase[value - 10]
            answer = str(value) + answer
        print(answer)


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
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()
    # print(25 // 20)
    # encode(14, 14)
    # decode("J", 20)
