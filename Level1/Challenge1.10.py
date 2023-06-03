"""
An automorphic number is a number whose square ends with the same digits as the original number. For example,
5 is an automorphic number because 5^2 = 25 and the last digit of 25 is 5, which is the same as the original number.

Write a function called is_automorphic that takes an integer n as input
and returns True if n is an automorphic number
and False otherwise.

Input: is_automorphic(5)

Expected output: True
"""


def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))


print(is_automorphic(5))
