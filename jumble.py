words = ["tefon", "sokik","niumem", "siconu"] # Test input (only one possible anagram)
indexes = [[2,4], [0,1,3], [4], [3,4]] # Test indexes

# Last word = _ _   _ _ _ _ _ _

def dictionary():
    """
    Create a dictionary [word: [anagram(word)]]
    Runtime: O(n^2 * log n) For loop and nested sort.
    """
    dict = {}
    file = open("/usr/share/dict/words", "r")   # O(1)
    for word in file:                           # O(n) for loop
        word = word.strip().lower()             # O(n) lower
        sorted_word = ''.join(sorted(word))     # O(n log n) sorting
        if sorted_word in dict:                 # O(1)
            if word not in dict[sorted_word]:   # O(1)
                dict[sorted_word].append(word)  # O(1)
        else:
            dict[sorted_word] = [word]          # O(1)
    return dict

dict = dictionary()

def make_anagram():
    """
    Find all anagrams for the words.
    Runtime: O(n^2 * log n) For loop and nested sort.
    """
    anagrams = []
    for word in words:                  # O(n)
        word = "".join(sorted(word))    # O(n log n)
        anagram = dict[word]            # O(1)
        anagrams.append(anagram)        # O(1)
    return anagrams # [['often'], ['kiosk'], ['immune'], ['cousin']]


def find_letters():
    """
    Find the letters at the provided indexes.
    Runtime: O(n^2 * log n)
    """
    letters = ""
    anagrams = make_anagram()           # O(n^2 * log n)
    for i in range(len(anagrams)):      # O(n)
        for index in indexes[i]:        # O(n)
            word = anagrams[i][0]       # O(1)
            letters += word[index]      # O(1)
    return letters                      # O(1)

# def find_first_two_letters():
#     letters = find_letters()
#     temp_letters = letters
#     counter = 0
#     permutations = []
#     for letter in letters:
#         if counter + 1 == len(letters):
#             pass # Should stop func
#         else:
#             test = dict[letter + letters[counter]]
#             permutations.append(dict[letter + letters[counter]])
#         counter += 1
#
#     return permutations
# words = ["tefon", "sokik","niumem", "siconu"]
# indexes = [(2,4), (0,1,3), (4), (3,4)]

def find_sentence():
    pass

print(find_first_two_letters())
