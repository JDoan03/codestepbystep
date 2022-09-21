# Write a function named abs_sum that takes a list of integers as a parameter
# and returns the sum of the absolute values of each element in the list. For
# example, the absolute sum of [-1, 2, -4, 6, -9] is 22. If the list is empty,
# return 0.

# Use Python's functional programming constructs, such as list comprehensions,
# map, filter, reduce, to implement your function. Do not use any loops or
# recursion in your solution.


def abs_sum(lst):
    i = 0
    summ = 0
    if len(lst) == 0:
        return summ


    else:
        from functools import reduce
        summ = reduce(lambda x, y: x + y if x >= 0 and y >= 0 else x + (y * -1), lst, 0)
        return summ




print(abs_sum([0, 1, 2]))
print(abs_sum([0, -1, 2]))
print(abs_sum([]))
