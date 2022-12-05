import string

with open("input.txt") as f:
    rs = f.readlines()

rs = [item_list.strip("\n") for item_list in rs]


# Return a bag contents as a set
def bag_as_set(rs_contents):
    return set(rs_contents)

def priority_value(item):
    # Generate the alphabet
    alphabet = list(string.ascii_letters)
    alphabet.insert(0, "") # Cheat and put a blank at the start to index from 1
    return alphabet.index(item.pop())


total = 0

# Loop through rucksacks list
for i in range(len(rs)):

    if i % 3 == 0:
        # Make a group of elves
        group = [bag_as_set(rs[i]), bag_as_set(rs[i+1]), bag_as_set(rs[i+2])]

        # Which one is in all three? (this is a set)
        common = group[0].intersection(group[1]).intersection(group[2])

        print(common)

        # Add its value to the total
        total += priority_value(common)


print(total)



