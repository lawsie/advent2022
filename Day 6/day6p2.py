with open("input.txt") as f:
    comms = f.readline().rstrip()


if __name__ == "__main__":
    start = 0
    end = 14
    slice = comms[start:end]

    while len(set(slice)) < 14:
        start +=1
        end += 1
        slice = comms[start:end]
        print(slice)
    
    print(end)