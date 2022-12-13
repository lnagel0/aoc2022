import math

input = open("input.txt", encoding="utf-8")

instructions = []
hx, hy, tx, ty = 0, 0, 0, 0
dx, dy = 0, 0
visited = set()

for line in input:
    instructions.append(line.rstrip())

for line in instructions:
    dir, amt = line.split(' ')

    for i in range(int(amt)):
        if dir == 'R':
            hx += 1
        elif dir == 'L':
            hx -= 1
        elif dir == 'U':
            hy -= 1
        elif dir == 'D':
            hy += 1
    
        dx, dy = hx - tx, hy - ty
        if abs(dx) > 1 or abs(dy) > 1:
            if dx:
                tx += math.copysign(1, dx)
            if dy:
                ty += math.copysign(1, dy)

            visited.add((tx, ty))    

print(len(visited))