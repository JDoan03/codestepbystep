# Write a function named dice_sum that prompts the user for a desired sum,
# then repeatedly rolls two six-sided dice until their sum is the desired sum.
# Here is the expected dialogue with the user:
#
# Desired dice sum: 9
# 4 and 3 = 7
# 3 and 5 = 8
# 5 and 6 = 11
# 5 and 6 = 11
# 1 and 5 = 6
# 6 and 3 = 9
#
# (Because this problem uses random numbers, our test cases check only the
# general format of your output. You must still examine the output yourself to
# make sure the answer is correct.)


import random


def dice_sum():

    isSolved = False
    desiredSum = int(input("Desired dice sum: "))
    if desiredSum < 1 or desiredSum > 12:
        print("Please enter a number 1-12")

    while not isSolved:
        num1 = random.randint(1, 6)
        num2 = random.randint(1, 6)
        adder = num1 + num2
        print("{} and {} = {}".format(num1, num2, adder))

        if adder == desiredSum:
            isSolved = True


dice_sum()