with open("input.txt") as f:
    rounds = f.readlines()

rounds = [round.strip("\n") for round in rounds]

shape_scores = {"rock":1, "paper":2, "scissors":3, "win":6,"draw": 3, "lose": 0}

def what_to_choose(their_move, need_to):
    draws = {
        "rock": {"lose":"scissors", "draw":"rock", "win":"paper"}, 
        "paper": {"lose":"rock", "draw":"paper", "win":"scissors"}, 
        "scissors": {"lose":"paper", "draw":"scissors", "win":"rock"}
    }
    return draws[their_move][need_to]

def translate(letter):
    name_map = {
        "A" : "rock","B" : "paper","C" : "scissors","X" : "lose","Y" : "draw","Z" : "win"
    }
    return name_map[letter]

total = 0

for round in rounds:
    move = round.split(" ")

    print("They chose " + translate(move[0]) + " and you need to " + translate(move[1]))
    your_choice = what_to_choose(translate(move[0]), translate(move[1]))
    print("You choose " + your_choice)
    print("Move points: " + str(shape_scores[your_choice]) )
    print("Win status points: " + str(shape_scores[translate(move[1])]) )
    total += shape_scores[your_choice] + shape_scores[translate(move[1])]

print(total)