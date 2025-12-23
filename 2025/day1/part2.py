import re

with open("./input.txt", "r") as f:
    puzzle_input = f.read()

currentPosition = 50
zeroCount = 0

for line in puzzle_input.splitlines():
    match = re.match(r'([LR])(\d+)', line)
    direction = match.group(1)
    distance = int(match.group(2))

    if direction == 'L' and currentPosition == 0:
        new_position = currentPosition - distance # leaving out the -100 is like doing "-1" to the calculated zero count
        print("turning left", currentPosition, "-", distance, "=", new_position)
    elif direction == 'L':
        new_position = currentPosition - 100 - distance
        print("turning left", currentPosition, "-", distance, "=", new_position)
    elif direction == 'R':
        new_position = currentPosition + distance
        print("turning right", currentPosition, "+", distance, "=", new_position)
    else:
        raise Exception("Invalid direction")

    zeroCount += abs(new_position) // 100
    currentPosition = new_position % 100

    print("calcuated new position:", currentPosition, "and total zero crossings:", zeroCount)
        
print("Number of times crossed position 0:", zeroCount)