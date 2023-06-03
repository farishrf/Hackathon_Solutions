"""
Write a function called Count_P that takes a string sentence as input
and counts the number of occurrences of the letter 'P' in the string.
The function should return the count of 'P' characters in the string.

Input: Count_P("PYSS PROGRAMMATHON")
Expected output: 2
"""


# This is a solution of a person who doesn't know that there exist a function .count()

def Count_P(sentence):
    counter = 0
    for letter in sentence:
        if letter == "P":
            counter += 1
    return counter


# Optimal solution
def Optimal_Count_P(sentence):
    return sentence.count("P")


print(Count_P("PYSS PROGRAMMATHON"))
print(Optimal_Count_P("PYSS PROGRAMMATHON"))
