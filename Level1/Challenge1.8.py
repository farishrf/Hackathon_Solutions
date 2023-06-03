"""
Write a function called Up_Down that takes a single number as its parameter.
The function should return a tuple containing two numbers
The first should be one lower than the parameter,
And the second should be one higher.

Input: Up_Down(7)

Expected Output: (6, 8)
"""


def Up_Down(a):
    # Note: by default python returns tuple if separated by commas, no need to put parentheses ()
    return a - 1, a + 1


print(Up_Down(7))
