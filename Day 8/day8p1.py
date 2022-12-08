with open("input.txt") as f:
    trees = [list(t.strip("\n")) for t in f.readlines()]

# Convert to integers
trees = [[int(num) for num in line] for line in trees]

# Find out some key info
GRID_HEIGHT = len(trees)
GRID_WIDTH = len(trees[0])

def check(tree_index, direction, trees):
    print("Checking", tree_index, "in direction", direction)

    t_row = tree_index[0]
    t_col = tree_index[1]

    match direction:
        case "up":
            visible = True
            for r in range(0, t_row): # Loop through until the row
                if trees[r][t_col] >= trees[t_row][t_col]:                    
                    visible = False  # Can't see it
            return visible
        
        case "down":
            visible = True
            for r in range(t_row+1, GRID_HEIGHT): # Loop through from row after until end
                if trees[r][t_col] >= trees[t_row][t_col]:                    
                    visible = False  # Can't see it
            return visible

        case "left":
            visible = True
            for c in range(0, t_col):
                if trees[t_row][c] >= trees[t_row][t_col]:
                    visible = False
            return visible
        
        case "right":
            visible = True
            for c in range(t_col+1, GRID_WIDTH):
                if trees[t_row][c] >= trees[t_row][t_col]:
                    visible = False
            return visible

        case _:
            print("Uh oh")


visible_trees = 0

# Loop through the rows of trees
for row in range(GRID_HEIGHT):

    # First and last rows are always visible
    if row == 0 or row == GRID_HEIGHT-1:
        visible_trees += GRID_WIDTH
        continue

    # Check the columns
    for col in range(GRID_WIDTH):
        
        # First and last cols always visible
        if col == 0 or col == GRID_WIDTH-1:
            visible_trees += 1
            continue

        # This is an inner tree
        this_tree = [row, col]
        can_see_it = check(this_tree, "down", trees) or check(this_tree, "up", trees) or check(this_tree, "left", trees) or check(this_tree, "right", trees)
        visible_trees += 1 if can_see_it else 0

print(visible_trees)