# String Algorithms
Github Lesson 3 ([link](https://github.com/Make-School-Courses/CS-1.3-Core-Data-Structures/blob/master/Lessons/StringAlgorithms.md))

[We spent the class finishing up the material from [class 2](classes/class2.md)]

# Homework
- Implement palindrome checking functions using [palindromes starter code]:
    - Implement `is_palindrome_iterative` - iterative version of `is_palindrome`
    - Implement `is_palindrome_recursive` - recursive version of `is_palindrome`
    - Run `python palindromes.py string1 string2 ... stringN` to test `is_palindrome`, for example:
        ```
        $ python palindromes.py ABC noon RaceCar 'Taco, Cat'
        FAIL: 'ABC' is not a palindrome
        PASS: 'noon' is a palindrome
        PASS: 'RaceCar' is a palindrome
        PASS: 'Taco, Cat' is a palindrome
        ```
    - Run `pytest palindromes_test.py` to run the [palindromes unit tests] and fix any failures
- Implement string searching functions (try both iterative and recursive versions) using [strings starter code]:
    - Implement `contains(text, pattern)` - a boolean indicating whether `pattern` occurs in `text`
    - Implement `find_index(text, pattern)` - the starting index of the first occurrence of `pattern` in `text`
    - Implement `find_all_indexes(text, pattern)` - a list of starting indexes of all occurrences of `pattern` in `text`
    - Run `python strings.py text pattern` to test string searching algorithms, for example:
        ```
        $ python strings.py 'abra cadabra' 'abra'
        contains('abra cadabra', 'abra') => True
        find_index('abra cadabra', 'abra') => 0
        find_all_indexes('abra cadabra', 'abra') => [0, 8]
        ```
    - Run `pytest strings_test.py` to run the [strings unit tests] and fix any failures
- Write additional test cases to expand the [strings unit tests] to ensure your string searching algorithms are robust
    - Include several test cases that are both positive (examples) and negative (counterexamples)
- Refactor functions to increase code reuse and avoid duplication ([DRY principle])
- Annotate functions with complexity analysis of running time and space (memory)

## Stretch Challenges
- Implement permutation generating functions (try both iterative and recursive versions)
- Implement anagram generating functions (try both iterative and recursive versions)
    - *Hint:* Use the Unix dictionary words list located at: `/usr/share/dict/words`
