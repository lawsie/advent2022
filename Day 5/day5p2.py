from queue import LifoQueue

# Import moves
with open("input.txt") as f:
    moves = f.readlines()
moves = [list_item.strip("\n") for list_item in moves]

with open("crates.txt") as f:
    crates = f.readlines()
crates = [line.strip("\n") for line in crates]


def parse_crates(crates, stacks):
    """ Parse the crates diagram into a list of stacks"""
    stacks = [LifoQueue() for x in range(stacks)]
    crates.reverse()    # Start at the bottom
  
    # Look at each of the rows of crates starting at the bottom row
    for r in range( len(crates) ):
        stack_number = 0
        for i in range(0, len(crates[r]), 4):
            letter = crates[r][i+1:i+2]

            # Don't add spaces (ascii 32) to the stack
            if ord(letter) != 32:
                stacks[stack_number].put(crates[r][i+1:i+2])
                #print("Adding ", letter, "(", ord(letter), ") to stack ", stack_number)
            stack_number += 1
    
    return stacks

def parse_instruction(instr_line):
    """Split an instruction into three integers - number of ops, stack from, stack to"""
    if instr_line is not None:
        instr = instr_line.split(" ")
        return int(instr[1]), int(instr[3])-1, int(instr[5])-1

def perform_instruction(line_of_text, stacks_list):
    """Execute a line of text instruction"""
    pop, from_stack, to_stack = parse_instruction(line_of_text)
    holding_bay = []
    for i in range(pop):
        # Keep all of the crates in a list
        holding_bay.append(stacks_list[from_stack].get())
    holding_bay.reverse()   # Add them in reverse
    for c in holding_bay:
        stacks_list[to_stack].put(c)


def display_stack(stack):
    """Show the state of a stack for debug purposes"""
    while not stack.empty():
        print(stack.get())
    
def top_crates(stacks):
    """Collate and return a string containing the letters of the top crates"""
    crate_string = ""
    for stack in stacks:
        crate_string += str(stack.get())
    return crate_string

    
if __name__ == "__main__":
    NUMBER_OF_STACKS = 9
    get_stacks = parse_crates(crates, NUMBER_OF_STACKS)
    for move in moves:
        perform_instruction(move, get_stacks)
    print( top_crates(get_stacks))

    
    

