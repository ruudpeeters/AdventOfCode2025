with open("full.txt", "r") as f:
    data = f.read().splitlines()

dial = 50
count = 0

for line in data:
    letter = line[0]
    number = int(line[1:])
    if letter == 'R':
        dial += number
    elif letter == 'L':
        dial -= number
    else:
        print("Invalid instruction:", line)

    dial = dial % 100
    if dial == 0:
        count += 1

print(count)
