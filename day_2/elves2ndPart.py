input = open("input.txt", encoding="utf-8")

inputCommands = []
counter = 0
elfPoints = 0
userPoints = 0

A, X = 'rock', 'rock'
B, Y = 'paper', 'paper'
C, Z = 'scissors', 'scissors'

for line in input:
    inputCommands.append(line.rstrip())

# Elf winning cases: B, X / C, Y / A, Z
# User winning cases: C, X / A, Y / B, Z

# Losses: A, X / B, X / C, X
# Draws: A, Y / B, Y / C, Y
# Wins: A, Z / B, Z / C, Z

for round in inputCommands:
    counter += 1
    # Losing cases:
    if round == ('A' + ' ' + 'X'):
        userPoints += 3
        elfPoints += 7
    elif round == ('B' + ' ' + 'X'):
        userPoints += 1
        elfPoints += 8
    elif round == ('C' + ' ' + 'X'):
        userPoints += 2
        elfPoints += 9
    # Draw cases:
    elif round == ('A' + ' ' + 'Y'):
        userPoints += 4
        elfPoints += 4
    elif round == ('B' + ' ' + 'Y'):
        userPoints += 5
        elfPoints += 5
    elif round == ('C' + ' ' + 'Y'):
        userPoints += 6
        elfPoints += 6
    # Win cases:
    elif round == ('A' + ' ' + 'Z'):
        userPoints += 8
        elfPoints += 1
    elif round == ('B' + ' ' + 'Z'):
        userPoints += 9
        elfPoints += 2
    elif round == ('C' + ' ' + 'Z'):
        userPoints += 7
        elfPoints += 3
    
print(elfPoints, userPoints)

input.close()