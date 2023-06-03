"""
Write a function called Range that takes a list of integers a as input
and calculates the difference between the largest and smallest values in the list.
The function should return the result.

Input: Range([1, 8, 2, 9, 3, -10, 90, 20])

Expected Output: 100
"""


def Range(a):
    return max(a) - min(a)  # returns the difference between the max and min


print(Range([1, 8, 2, 9, 3, -10, 90, 20]))
