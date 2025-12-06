with open("full.txt") as f:
    data = f.read().split(',')

count = 0

for entry in data:
    start, end = entry.split('-')
    if len(start) == len(end) and len(start) % 1 == 1:
        continue
    for i in range(int(start), int(end)+1):
        s = str(i)
        # print(i, round(len(s)/2))
        for split_length in range(1, round(len(s)/2) + 1):
            # print("Using split length:", split_length)
            if len(s) % split_length != 0:
                continue

            s_split = [s[a*split_length:(a+1) * split_length] for a in range(int(len(s)/split_length))]
            if all([s_split[0] == s_split_entry for s_split_entry in s_split]):
                count += i
                break

print(count)