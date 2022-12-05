import string

with open("input.txt") as f:
    rs = f.readlines()

rs = [item_list.strip("\n") for item_list in rs]


# Separate the given rucksack string into two sets (i.e. get rid of duplicates)
def separate(rs_contents):
    return set(rs_contents[:int(len(rs_contents)/2)]), set(rs_contents[int(len(rs_contents)/2):])

def priority_value(item):
    # Generate the alphabet
    alphabet = list(string.ascii_letters)
    alphabet.insert(0, "") # Cheat and put a blank at the start to index from 1
    return alphabet.index(item.pop())


total = 0

for item in rs:
    # Get two sets of all items in the compartments 
    c1, c2 = separate(item)

    # Which one is in both? (this is a set)
    common = c1.intersection(c2)

    # Add its value to the total
    total += priority_value(common)


print(total)



