"""
Write a function My_Calc that takes two integers and an arithmetic operator as input,
and returns the result of performing the arithmetic operation on the two integers.
The function should support the four basic arithmetic operators (+, -, *, /).
If the operator is not one of the supported operators, the function should return None.

Input: My_Calc(5, '*', 3)
Expected output: 15
"""


def My_Calc(first_int, operator, second_int):
    result = None
    if operator == '*':
        result = first_int * second_int
    elif operator == '/':
        result = first_int / second_int
    elif operator == '+':
        result = first_int + second_int
    elif operator == '-':
        result = first_int - second_int
    return result


print(My_Calc(5, '*', 3))
print(My_Calc(4, '-', 3)) # to test other cases
