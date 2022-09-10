# Write a function named num_unique_values that accepts a list of integers
# as a parameter and returns the number of unique integer values in the list.
# For example, if a list named l contains the values
# [3, 7, 3, -1, 2, 3, 7, 2, 15, 15], the call of num_unique_values(l) should
# return 5. If passed the empty list, you should return 0. Use a set as
# auxiliary storage to help you solve this problem. Do not modify the list passed
# in.

def num_unique_values(numbers):

    aList = []
    if len(numbers) == 0:
        return 0
    for x in numbers:
        if x not in aList:
            aList.append(x)
    return len(aList)


num_unique_values([3, 7, 3, -1, 2, 3, 7, 2, 15, 15])  # 5
num_unique_values([4, 2, 4, 2, 4, 4, 4, 2, 2, 2])  # 2
num_unique_values([42, 42, 42, 42, 42])  # 1
num_unique_values([42])  # 1
num_unique_values([])  # 0