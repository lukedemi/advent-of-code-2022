from collections import defaultdict


input_file = "inputs/day07.txt"
# input_file = "example.txt"
with open(input_file) as f:
    data = [line.strip() for line in f]

dir_sizes = defaultdict(int)
current_dirs = []
for i in range(len(data)):
    line = data[i]
    if line[0] == "$":
        argv0 = line.split()[1]

        if argv0 == "ls":
            # lookahead to all the files in the dir
            for j in range(i + 1, len(data)):
                files = data[j]

                if files[0] == "$":
                    break
                elif files.split()[0] == "dir":
                    pass
                else:
                    size = int(files.split()[0])
                    name = files.split()[1]
                    for directory in current_dirs:
                        dir_sizes[directory] += size
        elif argv0 == "cd":
            argv1 = line.split()[2]
            if argv1 == "..":
                current_dirs = current_dirs[:-1]
            elif argv1 == "/":
                current_dirs = ["/"]
            else:
                current_dirs.append(current_dirs[-1] + "/" + argv1)

sorted_dir_sizes = {
    k: v for k, v in sorted(dir_sizes.items(), key=lambda item: item[1])
}

min_needed = abs(70000000 - sorted_dir_sizes["/"] - 30000000)

file_to_delete = None
baby_dir_sizes = 0
for directory, size in sorted_dir_sizes.items():
    if size > min_needed and not file_to_delete:
        file_to_delete = size

    if size > 100000:
        continue

    baby_dir_sizes += size

print("part 1:")
print(baby_dir_sizes)
print("part 2:")
print(file_to_delete)
