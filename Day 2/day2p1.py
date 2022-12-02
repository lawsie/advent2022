with open("input.txt") as f:
    rounds = f.readlines()

rounds = [round.strip("\n") for round in rounds]

shape_scores = {"X":1, "Y":2, "Z":3}

combos = {
    "A" : { "X": 3, "Y":6, "Z":0},
    "B" : { "X": 0, "Y":3, "Z":6},
    "C" : { "X": 6, "Y":0, "Z":3},
}

total = 0

for round in rounds:
    move = round.split(" ")
    total += shape_scores[move[1]] + combos[move[0]][move[1]]

print(total)