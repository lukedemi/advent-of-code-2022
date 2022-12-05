import copy

input_file = "inputs/day05.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line for line in f]

stack_lines = []
instructions = []
reading_instructions = False
for line in data:
    if line.strip() == "":
        reading_instructions = True
    elif reading_instructions:
        instructions.append(line.strip())
    else:
        stack_lines.append(line)

stacks = []
stack_lines.reverse()
for i in range(len(stack_lines[0])):
    letters = []
    for line in stack_lines[1:]:
        if line[i].isalpha():
            letters.append(line[i])

    if len(letters) > 0:
        stacks.append(letters)

stacks9000 = copy.deepcopy(stacks)
stacks9001 = copy.deepcopy(stacks)
for instruction in instructions:
    movements = int(instruction.split()[1])
    from_stack = int(instruction.split()[3]) - 1
    to_stack = int(instruction.split()[-1]) - 1

    for movement in range(movements):
        moved_crate = stacks9000[from_stack].pop()
        stacks9000[to_stack].append(moved_crate)

    crates = stacks9001[from_stack][-movements:]
    stacks9001[from_stack] = stacks9001[from_stack][:-movements]
    stacks9001[to_stack].append(crates)
    stacks9001[to_stack] = [
        item for sublist in stacks9001[to_stack] for item in sublist
    ]


part1 = ""
for stack in stacks9000:
    part1 += stack[-1]

part2 = ""
for stack in stacks9001:
    part2 += stack[-1]

print("part 1:")
print(part1)
print("part 2:")
print(part2)
