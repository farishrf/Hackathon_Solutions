"""
Write a function called missing_num that takes a list of integers as input,
and returns the missing number from the list.
The function should compare the input list with a pre-defined list of integers from 1 to 10
and return the number that is missing from the input list.

Input: missing_num([1,2,3,4,6,7,8,9,10])
Expected output: 5
"""


def missing_num(a):
    ready_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    not_exist = []
    for i in ready_list:
        if i in a:
            pass
        else:
            not_exist.append(i)
    return not_exist[0]


"""
Using the mathematical formula for the sum of the first n integers to compute the expected sum of the input list,
and then subtracting the actual sum of the input list to find the missing number.
"""


def optimal_missing_num(a):
    expected_sum = sum(range(1, 11))
    actual_sum = sum(a)
    return expected_sum - actual_sum


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(optimal_missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
