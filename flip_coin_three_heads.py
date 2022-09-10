# Write a function named flip_coin_three_heads that repeatedly flips a coin
# until three heads in a row are seen. You should use a Random object to give
# an equal chance to a head or a tail appearing. Each time the coin is
# flipped, what is seen is displayed (H for heads, T for tails). When 3 heads
# in a row are flipped a congratulatory message is printed. Here is a possible
# output of a call to your function:
#
# T T T H T H H H
# Three heads in a row!
#
# (Because this problem uses random numbers, our test cases check only the
# general format of your output. You must still examine the output yourself
# to make sure the answer is correct.)


import random


def flip_coin_three_heads():
    headCounter = 0

    while headCounter != 3:
        num1 = random.randint(0, 1)
        if num1 == 1:
            print("T", end=" ")
            headCounter = 0
        else:
            print("H", end=" ")
            headCounter += 1

    print("")
    print("Three heads in a row!")


flip_coin_three_heads()
