input_file = "inputs/day06.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line for line in f]


def find_start(data, distinct):
    chars = []
    for char in data:
        chars.append(char)

        if not len(chars) >= 4:
            continue

        start_of_message = chars[-distinct:]

        if len(start_of_message) == len(set(start_of_message)):
            return len(chars)


print("part 1:")
print(find_start(data[0], 4))
print("part 2:")
print(find_start(data[0], 14))
