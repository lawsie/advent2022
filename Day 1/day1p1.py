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

print(max(elves))