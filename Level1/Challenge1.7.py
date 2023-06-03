"""
Write a function called Single_Status that takes a dictionary
and returns the number of Singles in the dictionary.

Input:

Single_Status({
    "Ali": "Single",
    "Sarra": "Married",
    "Sami": "Single"
})

Expected output: 2
"""

statuses = {
    "Ali": "Single",
    "Sarra": "Married",
    "Sami": "Single"
}


def Single_Status(dic):
    single_counter = 0
    for key, value in dic.items():
        if value == 'Single':
            single_counter += 1
    return single_counter


def Optimal_Single_Status(dic):
    # Using list comprehension
    return len([value for value in dic.values() if value == "Single"])


print(Single_Status(statuses))
print(Optimal_Single_Status(statuses))
