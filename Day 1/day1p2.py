with open("input.txt") as f:
    cals = f.readlines()


elves = []

curr = 0

for cal in cals:
    if cal == "\n":
        elves.append(curr)
        curr = 0
    else:  
        curr += int(cal)


elves.sort(reverse=True)

total = sum([elves[i] for i in range(3)])

print(total)