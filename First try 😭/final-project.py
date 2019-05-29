# Scenario 1: One-time route cost check
# You have a carrier route list with 100,000 (100K) entries (in arbitrary order) and a single phone number.
# How quickly can you find the cost of calling this number?

# SOLUTION 1:
    # REORDER LONG list

    # USE BINARY SEARCH TO Find


# SOLUTION 2:
    # CREATE TOUPLE [(NUMBER, PRICE),(NUMBER2, PRICE2)] { NUMBER:PRICE }
    # CREAte a list of all the keys that have the first number ( Rinse Clean Repeat )

    list_of_phone_numbers = dictionary.keys()

    for number in list_of_phone_numbers:
        if number[current_recursion_count] == given_number[current_recursion_count]
