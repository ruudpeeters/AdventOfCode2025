with open("full.txt", "r") as f:
    data = f.read().splitlines()
    
dial = 50    
count = 0

for line in data:
    letter = line[0]
    number = int(line[1:])
    print(line)
    if letter == 'R':
        dial += number
    elif letter == 'L':
        if dial == 0:
            count -= 1
        dial -= number
    else:
        print("Invalid instruction:", line)
    
    print("dial start", dial)
    if dial == 0:
        count += 1
    while (dial > 99 or dial < 0):
        if dial > 99:
            dial -= 100
            count += 1
        if dial < 0:
            dial += 100
            count += 1
        print("dial position", dial)
    
    print("Final dial", dial, count)
    print()

print(count)
