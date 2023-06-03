"""
NOT SURE:
Write a function called Makes_10 that takes two integers a and b as input
and returns True if either of them is 10 or if their sum is 10.
Otherwise, the function should return False.

Input: Makes_10(7, 3)
Expected Output: True
"""


def Makes_10(a, b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


print(Makes_10(10, 3))
