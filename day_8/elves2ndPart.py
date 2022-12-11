input = open("input.txt", encoding="utf-8")

parsedInput = []
array2d = [] # rows
array2d2 = [] # columns
i = 0
j = 0
score = []
numbers = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
coords = set()

for line in input:
    parsedInput.append(line.rstrip())

for line in parsedInput:
    arr = []
    for char in line:
        arr.append(int(char))
    array2d.insert(i, arr)
    i += 1

for l in range(len(array2d)):
    array2d2.append([])
    for x in range(len(array2d)):
        array2d2[l].append(array2d[x][l])

def moveDown(array, row, column):
    if row < len(array2d[0])-1:
        return array[row+1][column], moveDown(array, row+1, column)
    else: return

def moveUp(array, row, column):
    if row > 0:
        return array[row-1][column], moveUp(array, row-1, column)
    else: return

def moveRight(array, row, column):
    if column < len(array2d[0])-1:
        return array[row][column+1], moveRight(array, row, column+1)
    else: return

def moveLeft(array, row, column):
    if column > 0:
        return array[row][column-1], moveLeft(array, row, column-1)
    else: return

def clarify(input):
    result = []
    for char in str(input):
        if char in numbers:
            result.append(int(char))
    return result

for t in range(len(array2d)):
    for x in range(len(array2d)):
        highestTree = array2d[t][x]
        rightMultiplier = 0
        leftMultiplier = 0
        downMultiplier = 0
        upMultiplier = 0

        treesToRight = clarify(moveRight(array2d, t, x))
        treesToLeft = clarify(moveLeft(array2d, t, x))
        treesToDown = clarify(moveDown(array2d, t, x))
        treesToUp = clarify(moveUp(array2d, t, x))

        for tree in treesToRight:
            if tree < highestTree:
                rightMultiplier += 1
            elif tree >= highestTree:
                rightMultiplier += 1
                break

        for tree in treesToLeft:
            if tree < highestTree:
                leftMultiplier += 1
            elif tree >= highestTree:
                leftMultiplier += 1
                break

        for tree in treesToDown:
            if tree < highestTree:
                downMultiplier += 1
            elif tree >= highestTree:
                downMultiplier += 1
                break

        for tree in treesToUp:
            if tree < highestTree:
                upMultiplier += 1
            elif tree >= highestTree:
                upMultiplier += 1
                break
        
        total = rightMultiplier * leftMultiplier * upMultiplier * downMultiplier
        score.append(total)

score.sort()
print(score)