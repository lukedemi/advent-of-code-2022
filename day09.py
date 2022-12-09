input_file = "inputs/day09.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line.strip() for line in f]


DIRECTIONS = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}


class Rope:
    def __init__(self):
        self.tail = [(0, 0)] * 10
        self.locations = []

        for knot in self.tail:
            self.locations.append(set())

    def head_loc(self):
        return self.tail[0]

    def move_head(self, direction):
        self.tail[0] = (
            self.head_loc()[0] + DIRECTIONS[direction][0],
            self.head_loc()[1] + DIRECTIONS[direction][1],
        )

    def follow(self, my_index, index_to_follow):
        y_diff = 0
        x_diff = 0

        # same location
        if (
            self.tail[index_to_follow][0] == self.tail[my_index][0]
            and self.tail[index_to_follow][1] == self.tail[my_index][1]
        ):
            return
        # on same plane
        elif (
            self.tail[index_to_follow][0] == self.tail[my_index][0]
            or self.tail[index_to_follow][1] == self.tail[my_index][1]
        ):

            # adjacent - do nothing!
            if (
                abs(self.tail[index_to_follow][1] - self.tail[my_index][1])
                + abs(self.tail[index_to_follow][0] - self.tail[my_index][0])
                == 1
            ):
                return

            if self.tail[index_to_follow][0] == self.tail[my_index][0]:
                if self.tail[index_to_follow][1] - self.tail[my_index][1] > 0:
                    x_diff = 1
                else:
                    x_diff = -1
            else:
                if self.tail[index_to_follow][0] - self.tail[my_index][0] > 0:
                    y_diff = 1
                else:
                    y_diff = -1

        elif (
            self.tail[index_to_follow][0] != self.tail[my_index][0]
            and self.tail[index_to_follow][1] != self.tail[my_index][1]
        ):
            # adjacent diagonally - break!
            if (
                abs(self.tail[index_to_follow][1] - self.tail[my_index][1])
                + abs(self.tail[index_to_follow][0] - self.tail[my_index][0])
                == 2
            ):
                return

            if self.tail[index_to_follow][1] - self.tail[my_index][1] > 0:
                x_diff = 1
            else:
                x_diff = -1
            if self.tail[index_to_follow][0] - self.tail[my_index][0] > 0:
                y_diff = 1
            else:
                y_diff = -1

        self.tail[my_index] = (
            self.tail[my_index][0] + y_diff,
            self.tail[my_index][1] + x_diff,
        )


rope = Rope()

for instruction in data:
    direction = instruction.split()[0]
    steps = int(instruction.split()[1])

    for step in range(steps):
        rope.move_head(direction)

        for k in range(len(rope.tail[:-1])):
            rope.follow(k + 1, k)
            rope.locations[k + 1].add(rope.tail[k + 1])


print("part 1:")
print(len(list(rope.locations[-1])))
print("part 2:")
print(len(list(rope.locations[1])))
