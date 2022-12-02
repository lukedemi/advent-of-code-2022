# "boilerplate" to get input
with open("inputs/day01.txt") as f:
    data = [line.strip() for line in f]

elves = []
current_elf = 0
for calories in data:
    print(calories)
    if calories == "":
        elves.append(current_elf)
        current_elf = 0
    else:
        current_elf += int(calories)

# add the last elf
elves.append(current_elf)

print("part 1:")
print(max(elves))
print("part 2:")
print(sum(sorted(elves)[-3:]))
