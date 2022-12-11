input = open("input.txt", encoding="utf-8")

instructions = []
grid = []

for y in range(5): # a 6x5 grid is built here
    grid.append([])
    for x in range(6):
        grid[y].append('.')

grid[4][0] = 'S'

for line in input:
    instructions.append(line.rstrip())

for x in range(5): # grid
    print(grid[x])