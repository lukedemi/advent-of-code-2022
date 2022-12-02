# "boilerplate" to get input
with open("inputs/day02.txt") as f:
    data = [line.strip() for line in f]

# I'm sorry about this solution but there's only 9 outcomes so
# it just felt right to hard code them

# A, X = Rock (1)
# B, Y = Paper (2)
# C, Z = Scissors (3)

# 6 = win
# 3 = draw
# 0 = loss
outcomes_part1 = {
    "A X": 3 + 1,
    "A Y": 6 + 2,
    "A Z": 0 + 3,
    "B X": 0 + 1,
    "B Y": 3 + 2,
    "B Z": 6 + 3,
    "C X": 6 + 1,
    "C Y": 0 + 2,
    "C Z": 3 + 3,
}

# A = Rock (1)
# B = Paper (2)
# C = Scissors (3)

# Y = draw (3)
# X = lose (0)
# Z = win (6)
outcomes_part2 = {
    "A X": 0 + 3,  # lose C
    "A Y": 3 + 1,  # draw A
    "A Z": 6 + 2,  # win B
    "B X": 0 + 1,  # lose A
    "B Y": 3 + 2,  # draw B
    "B Z": 6 + 3,  # win C
    "C X": 0 + 2,  # lose B
    "C Y": 3 + 3,  # draw C
    "C Z": 6 + 1,  # win A
}

part1_score = 0
part2_score = 0
for game in data:
    part1_score += outcomes_part1[game]
    part2_score += outcomes_part2[game]

print("part 1:")
print(part1_score)
print("part 2:")
print(part2_score)
