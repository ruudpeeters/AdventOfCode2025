from typing import Tuple


def parse_line(dir: str, turns: int, starting_position: int) -> Tuple[int, int]:
    position = starting_position
    line_count = 0

    for i in range(turns):
        if dir == "L":
            position -= 1
        elif dir == "R":
            position += 1
        else:
            raise ValueError("Unknown direction")

        if position > 99:
            position -= 100
        elif position < 0:
            position += 100

        if position == 0:
            line_count += 1

    return line_count, position


with open("test.txt", "r") as f:
    data = f.read().splitlines()

dial = 50
count = 0

for line in data:
    letter = line[0]
    number = int(line[1:])

    l_count, dial = parse_line(letter, number, dial)
    count += l_count

print(count)
