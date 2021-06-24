from itertools import product
with open("inputs/day02.txt") as file:
    data = list(map(int, file.readline().split(",")))


def run(memory, noun, verb):
    pointer = 0
    memory[1], memory[2] = noun, verb

    while True:
        opcode = memory[pointer]
        x, y = memory[memory[pointer + 1]], memory[memory[pointer + 2]]

        if opcode == 1:
            memory[memory[pointer + 3]] = x + y

        elif opcode == 2:
            memory[memory[pointer + 3]] = x * y

        elif opcode == 99:
            break

        pointer += 4

    return memory[0]


# Part 1 ===
part1 = run(data.copy(), 12, 2)


# Part 2 ===
part2 = None

for test_noun, test_verb in product(range(0, 100), range(0, 100)):
    if run(data.copy(), test_noun, test_verb) == 19690720:
        part2 = 100 * test_noun + test_verb
        break


print("Part 1:", part1)
print("Part 2:", part2)
