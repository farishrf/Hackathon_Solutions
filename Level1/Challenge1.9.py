"""
Write a function called Only_Integers that takes two inputs num1 and num2,
That returns True if both inputs are integers, and False otherwise.

Input: Only_Integers(1, 2)
Expected output: True

Input: Only_Integers(1, "2")
Expected output: False

"""


def Only_Integers(num1, num2):
    return type(num1) == int and type(num2) == int


print(Only_Integers(1, 2))
