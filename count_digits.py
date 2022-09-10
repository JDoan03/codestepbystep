# Write a function named count_digits that accepts an integer parameter and
# returns the number of digits in that integer. For example, count_digits(38015)
# returns 5. For negative numbers, return the same value as if the number were
# positive. For example, count_digits(-72) returns 2.


def count_digits(num):
    digits = 0
    if num < 0:
        num *= -1
    while num > 0:
        num = num // 10
        digits += 1
    return digits


count_digits(29107)  # 5
count_digits(456)  # 3
count_digits(9999999)  # 7
count_digits(48)  # 2
count_digits(120011021)  # 9
count_digits(2000000000)  # 10
count_digits(5)  # 1
count_digits(-3)  # 1
count_digits(-15)  # 2
count_digits(-29107)  # 5
