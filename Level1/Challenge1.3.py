"""
You are given a function named Football_Points which takes three integers wins, draws, and losses as input
representing the number of wins, draws, and losses a football team has accumulated in a season.
The function calculates the total number of points the team has earned based on the standard scoring system,
where a win is worth 3 points, a draw is worth 1 point, and a loss is worth 0 points.

Football_Points(3, 4, 1)
Expected output:
13
"""


def Football_Points(wins, draws, losses):
    if wins < 0 or draws < 0 or losses < 0:
        return None
    return wins * 3 + draws * 1 + losses * 0


print(Football_Points(3, 4, 1))
print(Football_Points(5, 0, 2))
print(Football_Points(0, 0, 1))
