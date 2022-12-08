from functools import reduce

input_file = "inputs/day08.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line.strip() for line in f]


class Tree:
    def __init__(self, coords):
        self.coords = coords


def is_on_edge(coords):
    y = coords[0]
    x = coords[1]
    if y == 0 or x == 0 or y + 1 == len(data) or x + 1 == len(data[y]):
        return True
    return False


def is_valid_coords(coords, xlen, ylen):
    y = coords[0]
    x = coords[1]
    if y < 0 or x < 0:
        return False
    elif y > ylen - 1 or x > xlen + -1:
        return False
    return True


highest_view_score = 0
trees_on_edge = 0
visible = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        height = data[y][x]

        if is_on_edge((y, x)):
            trees_on_edge += 1
        else:
            edge = False
            view_scores = []

            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                new_coords = (y, x)
                view_score = 0

                while True:
                    new_coords = (
                        new_coords[0] + direction[0],
                        new_coords[1] + direction[1],
                    )

                    # if new coords aren't valid - tree must be on edge
                    if not is_valid_coords(new_coords, len(data), len(data[y])):
                        edge = True
                        break

                    # if the next tree is bigger or equal to height
                    # end without visibility but with a view
                    if data[new_coords[0]][new_coords[1]] >= height:
                        view_score += 1
                        break

                    # if we didn't run into an edge or a bigger tree, add to the view score
                    view_score += 1

                view_scores.append(view_score)

            view_score = reduce(lambda x, y: x * y, view_scores)
            if view_score > highest_view_score:
                highest_view_score = view_score
            if edge:
                visible += 1


print("part 1:")
print(visible + trees_on_edge)
print("part 2:")
print(highest_view_score)
