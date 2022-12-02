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

for round in inputCommands:
    counter += 1
    # first, I check for ties:
    if round == ('A' + ' ' + 'X'):
        userPoints += 4
        elfPoints += 4
    elif round == ('B' + ' ' + 'Y'):
        userPoints += 5
        elfPoints += 5
    elif round == ('C' + ' ' + 'Z'):
        userPoints += 6
        elfPoints += 6
    # elf winning cases:
    elif round == ('B' + ' ' + 'X'):
        elfPoints += 8
        userPoints += 1
    elif round == ('C' + ' ' + 'Y'):
        elfPoints += 9
        userPoints += 2
    elif round == ('A' + ' ' + 'Z'):
        elfPoints += 7
        userPoints += 3
    #user winning cases:
    elif round == ('C' + ' ' + 'X'):
        elfPoints += 3
        userPoints += 7
    elif round == ('A' + ' ' + 'Y'):
        elfPoints += 1
        userPoints += 8
    elif round == ('B' + ' ' + 'Z'):
        elfPoints += 2
        userPoints += 9
    
print(elfPoints, userPoints)

input.close()