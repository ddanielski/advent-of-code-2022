import os


def play_outcome_part1(str_list, rule, game_points):
    p1 = rule[str_list[0]]
    p2 = str_list[1]
    if p1 == p2:
        return game_points["draw"] + game_points[tmp[1]]
    if (
       (p1 == "X" and p2 == "Y") or
       (p1 == "Y" and p2 == "Z") or
       (p1 == "Z" and p2 == "X")
       ):
        return game_points["won"] + game_points[tmp[1]]
    else:
        return game_points["lost"] + game_points[tmp[1]]


def play_outcome_part2(str_list, rule, game_points):
    p1 = str_list[0]
    p2 = str_list[1]
    tmp = game_points[rule[p2]]
    if rule[p2] == "won":
        if p1 == "A":
            return tmp + game_points["Y"]
        if p1 == "B":
            return tmp + game_points["Z"]
        if p1 == "C":
            return tmp + game_points["X"]
    elif rule[p2] == "lost":
        if p1 == "A":
            return tmp + game_points["Z"]
        if p1 == "B":
            return tmp + game_points["X"]
        if p1 == "C":
            return tmp + game_points["Y"]
    else:
        return tmp + game_points[rule[p1]]


rule = {"A": "X", "B": "Y", "C": "Z", "X": "lost", "Y": "draw", "Z": "won"}
game_points = {"won": 6, "draw": 3, "lost": 0, "X": 1, "Y": 2, "Z": 3}

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'day2.txt')) as f:
    lines = f.readlines()
    score = 0
    for line in lines:
        line = line.replace('\n', '')
        tmp = line.split(" ")
        score += play_outcome_part2(tmp, rule,
                                    game_points)
        print(str(play_outcome_part2(tmp, rule,
                                     game_points)))

print("The final score is: " + str(score))
