with open("input.txt") as f:
    ass = f.readlines()

ass = [list_item.strip("\n") for list_item in ass]


# Return an assignment as two lists of start and end
def two_ranges(assignment):
    elves = assignment.split(",")
    elves = [item.split("-") for item in elves]
    return[ range(int(item[0]), int(item[1])) for item in elves]

# What is the overlap between the two ranges
def overlap(range_list):

    x = range_list[0]
    y = range_list[1]

    ol = list(range(max(x.start, y.start), min(x.stop+1, y.stop+1), 1))
    return True if len(ol) > 0 else False # Was there an overlap?

total = 0

for i in range(len(ass)):

    # Is the range within the other range?
    if overlap(two_ranges(ass[i])):
        total += 1

print(total)

