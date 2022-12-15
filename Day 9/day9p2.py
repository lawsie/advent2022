# This doesn't work!

# Parse to a list of list of form ['A', 1]
with open("input_test.txt") as f:
    moves = [ [a[0], int(a[1])] for a in [t.strip("\n").split(" ") for t in f.readlines()]]
   

def move_head(currh, direction):
    """Calculate the new position of the head"""

    match direction:
        case 'U':
            currh[1] += 1
        case 'D':
            currh[1] -= 1
        case 'L':
            currh[0] -= 1
        case 'R':
            currh[0] += 1


def move_tail(curr, head):

    if curr == head:
        pass # Do nothing
    # Same col
    elif curr[0] == head[0]:
        if head[1] > curr[1]+1:
            curr[1] += 1
        elif head[1] < curr[1]-1:
            curr[1] -= 1
    # Same row
    elif curr[1] == head[1]:
        if head[0] > curr[0]+1:
            curr[0] += 1
        elif head[0] < curr[0]-1:
            curr[0] -= 1
    # Not in same row or column 
    elif curr[0] != head[0] and curr[1] != head[1]:

        print("Head", head[0], "tail", tail[0])

        # Are any of the distances away 2 or more
        delta0 = abs(curr[0]-head[0])
        delta1 = abs(curr[1]-head[1])

        if delta0 > 1 or delta1 > 1:

            # Find which way the head is
            up = True if head[1] > tail[1] else False
            down = True if head[1] < tail[1] else False
            left = True if head[0] < tail[0] else False
            right = True if head[0] > tail[0] else False

            if up:
                curr[1] += 1
                print("Move up")
            if down:
                curr[1] -= 1
                print("Move down")
            if left:
                curr[0] -= 1
                print("Move left")
            if right:
                curr[0] += 1
                print("Move right")
        
    
def visualise_knots(visited):
    # Define dimensions
    right = max([a[0] for a in visited])
    left = min([a[0] for a in visited])
    up = max([a[1] for a in visited])
    down = min([a[1] for a in visited])

    width = abs(right-left)+1
    height = abs(up-down)+1

    for i in range(height, -1, -1):
        for j in range(width):
            if [i, j] in visited:
                print("#",end="")
            else:
                print(".",end="")
        print("\n")


if __name__ == "__main__":

    # Set some constants for acessing the moves array
    DIR = 0
    SIZE = 1

    knots = [[0, 0] for i in range(10)]
    tail = knots[9]
    positions_visited = []

    test = [moves[0], moves[1], moves[2]]
    for move in test:

        print(move)
            
        # How many times to move? 
        for j in range(move[SIZE]):

            # Move the head
            move_head(knots[0], move[DIR])

            # Treat each subsequent knot in turn as a tail
            for i in range(1, len(knots)):
                print("Moving tail", i)
                move_tail(knots[i], knots[i-1])
                
            # When we're done moving, check if the tail went here  
            if tail not in positions_visited:
                positions_visited.append(tail.copy())
        
            print("Tail",tail)
        #print(knots)
        print("Done instruction --------------")

    print(positions_visited)    
    visualise_knots(positions_visited)
    



