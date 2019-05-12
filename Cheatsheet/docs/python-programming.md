## Python programming
* **Data types** (integer, float, and string)
* **Collections** (list, tuple, and dictionary), common operations
* **String manipulation** (indexing, slicing, splitting, and joining)

#### [String Manipulation](https://medium.com/@timothy.kaing/3ef411a2d88d "Article By Tim Kaing")
```Python
"""
String Manipulation
"""
string = "123456789"

for char in string:
  print(char) # 1,2,3,4,5,6...

one_to_five = string[0:5] # "12345"

five_to_nine = string[-5:] # "56789"

reverse_string = string[::-1] # "987654321"

one = string[0] # "1"

length = len(string) # 9

# Code by Tim Kaing
my_string = "I like turtles"

my_string.upper() # converts to "I LIKE TURTLES"

my_string.lowercase() # converts to "i like turtles"

my_string.title() # converts to "I Like Turtles"

my_string.swapcase() # converts to "i LIKE TURTLES"
```
