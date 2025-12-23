import re

with open("./input.txt", "r") as f:
    puzzle_input = f.read()


currentPosition = 50
zeroCount = 0

for line in puzzle_input.splitlines():
    match = re.match(r'([LR])(\d+)', line)
    direction = match.group(1)
    distance = int(match.group(2))

    if direction == 'L':
        currentPosition = (currentPosition - distance) % 100
    elif direction == 'R':
        currentPosition = (currentPosition + distance) % 100
    else:
        raise Exception("Invalid direction")
    
    if currentPosition == 0:
        zeroCount += 1
        
print("Number of times at position 0:", zeroCount)