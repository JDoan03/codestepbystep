# Write a function named count_negatives that takes a list of integers as a parameter and returns how many numbers in the list are negative. For example, if the list is [5, -1, -3, 20, 47, -10, -8, -4, 0, -6, -6], you should return 7.

# Use Python's functional programming constructs, such as list comprehensions, map, filter, reduce, to implement your function. Do not use any loops or recursion in your solution.

def double_list(lst):
    if len(lst) == 0:
        return []
    else:
        return list(map(lambda x: x * 2, lst))

print(double_list([2, -1, 4, 16]))