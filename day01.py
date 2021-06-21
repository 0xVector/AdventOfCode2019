with open("inputs/day01.txt") as file:
    data = [int(line.strip()) for line in file]


def fuel(mass):
    return mass // 3 - 2


# Part 1 ===
part1 = 0

for line in data:
    part1 += fuel(line)


# Part 2 ===
part2 = 0

for line in data:
    required = fuel(line)
    while required > 0:
        part2 += required
        required = fuel(required)


print("Part 1:", part1)
print("Part 2:", part2)
