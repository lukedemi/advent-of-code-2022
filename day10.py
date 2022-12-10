input_file = "inputs/day10.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line.strip() for line in f]


class Computer:
    def __init__(self):
        self.register = 1
        self.cycle = 0
        self.special_cycles = [20, 60, 100, 140, 180, 220]
        self.signal_strength = 0
        self.drawing = []

    def bump_cycle(self):
        self.cycle += 1
        if self.cycle in self.special_cycles:
            self.signal_strength += self.cycle * self.register

        draw = "."
        if (
            self.register - 1 <= (self.cycle % 40)
            and (self.cycle % 40) <= self.register + 1
        ):
            draw = "#"

        self.drawing.append(draw)

    def run_program(self, program):
        while True:
            if len(program) == 0:
                return

            instruction = program.pop(0)

            if instruction == "noop":
                self.bump_cycle()
            else:
                command, param = instruction.split()
                if command == "addx":
                    self.bump_cycle()
                    self.register += int(param)
                    self.bump_cycle()


computer = Computer()
computer.run_program(data)
print("part 1:")
print(computer.signal_strength)
print("part 2:")
start = 0
while start < len(computer.drawing):
    print("".join(computer.drawing)[start : start + 39])
    start += 40
