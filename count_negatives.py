# Write a function named count_negatives that takes a list of integers as a
# parameter and returns how many numbers in the list are negative. For
# example, if the list is [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6], you
# should return 7.
from functools import reduce


# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.

def count_negatives(lst):
    count = 0
    if len(lst) == 0:
        return 0
    else:

        count = len(list(filter(lambda x: x < 0, lst)))
        return count

print(count_negatives([-1, 2, -4, 6, -9]))
print(count_negatives([2, -1, 4, 16]))