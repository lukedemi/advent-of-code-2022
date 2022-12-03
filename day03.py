# "boilerplate" to get input
with open("inputs/day03.txt") as f:
    data = [line.strip() for line in f]


def item_priority(char):
    if char.isupper():
        return ord(char) - 64 + 26
    else:
        return ord(char) - 96


part1_priorities = 0
for contents in data:
    sack_size = int(len(contents) / 2)
    sack_1 = contents[:sack_size]
    sack_2 = contents[sack_size:]

    for char in list(set(sack_1).intersection(sack_2)):
        part1_priorities += item_priority(char)

part2_priorities = 0
for group in range((len(data) // 3)):
    rucksack_1 = data[(group * 3)]
    rucksack_2 = data[(group * 3) + 1]
    rucksack_3 = data[(group * 3) + 2]

    common_item = list(
        set(rucksack_1).intersection(rucksack_2).intersection(rucksack_3)
    )[0]
    part2_priorities += item_priority(common_item)

print("part 1:")
print(part1_priorities)
print("part 2:")
print(part2_priorities)
