# Write a function named num_in_common that accepts two lists of integers as
# parameters and returns the count of how many unique integers occur in both
# lists. For example, if two lists named l1 and l2 contains the values
# [3, 7, 3, -1, 2, 3, 7, 2, 15, 15] and [-5, 15, 2, -1, 7, 15, 36]
# respectively, your function should return 4 because the elements -1, 2, 7,
# and 15 occur in both lists. Use one or more sets as storage to help you
# solve this problem. Do not modify the lists passed in.


def num_in_common(l1, l2):
    return len(set(l1) & set(l2))


num_in_common([3, 7, 3, -1, 2, 3, 7, 2, 15, 15], [-5, 15, 2, -1, 7, 15, 36])  # 4
num_in_common([1, 2, 3], [3, 4, 5])  # 1
num_in_common([1, 2, 3], [2, 3, 4])  # 2
num_in_common([10, 20, 30, 40, 50], [50, 40, 30, 20, 10])  # 5
num_in_common([4], [1, 3, 5])  # 0
num_in_common([], [])  # 0
num_in_common([42], [])  # 0
num_in_common([], [42])  # 0