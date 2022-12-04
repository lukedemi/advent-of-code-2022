# "boilerplate" to get input
with open("inputs/day04.txt") as f:
    data = [line.strip() for line in f]

fully_contained = 0
partially_contained = 0
for assignment_pair in data:
    assignment_1 = assignment_pair.split(",")[0].split("-")
    assignment_2 = assignment_pair.split(",")[1].split("-")
    assignment_1 = set(range(int(assignment_1[0]), int(assignment_1[1]) + 1))
    assignment_2 = set(range(int(assignment_2[0]), int(assignment_2[1]) + 1))

    if assignment_1.issubset(assignment_2) or assignment_2.issubset(assignment_1):
        fully_contained += 1

    if len(assignment_1.intersection(assignment_2)) > 0:
        partially_contained += 1

print("part 1:")
print(fully_contained)
print("part 2:")
print(partially_contained)
