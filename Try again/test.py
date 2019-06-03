import string
import math

int_to_string = string.digits + string.ascii_lowercase
str_to_int = {string: index for index, string in enumerate(int_to_string)}

# print(str_to_int["1"])
number = 10
base = 2

lg_power = math.floor(math.log(number, base))

print(lg_power)
