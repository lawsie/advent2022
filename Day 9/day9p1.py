# Parse to a list of list of form ['A', 1]
with open("input.txt") as f:
    moves = [ [a[0], int(a[1])] for a in [t.strip("\n").split(" ") for t in f.readlines()]]
   

def move_head(curr, direction):
    """Calculate the new position of the head"""

    match direction:
        case 'U':
            curr[1] += 1
        case 'D':
            curr[1] -= 1
        case 'L':
            curr[0] -= 1
        case 'R':
            curr[0] += 1


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
        
    

    


if __name__ == "__main__":

    # Set some constants for acessing the moves array
    DIR = 0
    SIZE = 1

    head = [0, 0]
    tail = [0, 0]
    positions_visited = []


    for move in moves:
        print(move)
   
        # How many spaces to move? 
        for i in range(move[SIZE]):
            move_head(head, move[DIR])
            print("Head moves to", head)
            move_tail(tail, head)
            print("Tail is", tail)
            if tail not in positions_visited:
                positions_visited.append(tail.copy())

    print(len(positions_visited))    




