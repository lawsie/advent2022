from math import prod

with open("input.txt") as f:
    trees = [list(t.strip("\n")) for t in f.readlines()]

# Convert to integers
trees = [[int(num) for num in line] for line in trees]

# Find out some key info
GRID_HEIGHT = len(trees)
GRID_WIDTH = len(trees[0])

def scenic_score(tree_index, trees):
    
    t_row = tree_index[0]
    t_col = tree_index[1]

    scores = [0, 0, 0, 0]

    # Up
    for r in range(t_row-1, -1, -1): # Loop from tree to top
        scores[0] += 1 # Can see a tree
        if trees[r][t_col] >= trees[t_row][t_col]:                    
            break # Blocked
    
    # Left
    for c in range(t_col-1, -1, -1):
        scores[1] += 1
        if trees[t_row][c] >= trees[t_row][t_col]:
            break

    # Right          
    for c in range(t_col+1, GRID_WIDTH):
        scores[2] += 1
        if trees[t_row][c] >= trees[t_row][t_col]:
            break
    
    # Down
    for r in range(t_row+1, GRID_HEIGHT): # Loop from tree to bottom
        scores[3] += 1
        if trees[r][t_col] >= trees[t_row][t_col]:                    
            break

    print("Scores for", t_row, t_col, "are",scores)
    return prod(scores)
    

if __name__ == "__main__":

    high_score = 0

    # Loop through the rows of trees
    for row in range(GRID_HEIGHT):

        # Check the columns
        for col in range(GRID_WIDTH):

            # This is an inner tree
            this_tree = [row, col]
            high_score = max(scenic_score(this_tree, trees), high_score) # Replace if higher

    print(high_score)