input = open("input.txt", encoding="utf-8")

instructions = []
grid = []
currPos = [4, 0]

for y in range(5): # a 6x5 grid is built here
    grid.append([])
    for x in range(6):
        grid[y].append('.')

for line in input:
    instructions.append(line.rstrip())

def mvRight(currY, currX):
    grid[currY][currX + 1] = 'H'
    grid[currY][currX] = '.'
    currPos = [currY, currX + 1]
    return currPos

def mvLeft(currY, currX):
    grid[currY][currX - 1] = 'H'
    grid[currY][currX] = '.'
    currPos = [currY, currX - 1]
    return currPos

def mvUp(currY, currX):
    grid[currY - 1][currX] = 'H'
    grid[currY][currX] = '.'
    currPos = [currY - 1, currX]
    return currPos

def mvDown(currY, currX):
    grid[currY + 1][currX] = 'H'
    grid[currY][currX] = '.'
    currPos = [currY + 1, currX]
    return currPos

for instruction in instructions:
    input = instruction.split()
    dir, amt = input

    if dir == 'R':
        for i in range(int(amt)):
            currPos = mvRight(currPos[0], currPos[1])
    elif dir == 'L':
        for i in range(int(amt)):
            currPos = mvLeft(currPos[0], currPos[1])
    elif dir == 'U':
        for i in range(int(amt)):
            currPos = mvUp(currPos[0], currPos[1])
    elif dir == 'D':
        for i in range(int(amt)):
            currPos = mvDown(currPos[0], currPos[1])

for x in range(5): # grid
    print(grid[x])