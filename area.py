# Write a function named area that accepts the radius of a circle as a
# parameter and returns the area of a circle with that radius. For example,
# the call of area(2.0) should return 12.566370614359172. You may assume that
# the radius is non-negative.


import math


def area(circle_radius):
    return math.pi * circle_radius ** 2



area(1)  # 3.141592653589793
area(2)  # 12.566370614359172
area(12.34)  # 478.3879062809779
area(0)  # 0.0
