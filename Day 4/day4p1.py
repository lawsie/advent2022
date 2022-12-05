with open("input.txt") as f:
    ass = f.readlines()

ass = [list_item.strip("\n") for list_item in ass]


# Return an assignment as the start and end of ranges
def two_ranges(assignment):
    elves = assignment.split(",")
    elves = [item.split("-") for item in elves]
    return[ [int(item[0]), int(item[1])] for item in elves]

def within(first, second):
    if first[0] >= second[0] and first[1] <= second[1]:
        return True

total = 0

for i in range(len(ass)):
    # Get two ranges of the assignment
    ranges = two_ranges(ass[i])

    # Is the range within the other range?
    if within(ranges[0], ranges[1]) or within(ranges[1], ranges[0]):
        total += 1

print(total)