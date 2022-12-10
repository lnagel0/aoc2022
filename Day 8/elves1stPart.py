input = open("input.txt", encoding="utf-8")

parsedInput = []
array2d = []
array2d2 = []
i = 0
j = 0
highestTree = 0
totalSet = set()

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

def rowCheck(arrInput):
    treeSets = set()
    for i in range(len(arrInput)):
        if arrInput[i][0] >= 0:
            highestTree = arrInput[i][0]
            toAdd = str(i) + ',0'
            treeSets.add(toAdd)
        else:
            highestTree = 0

        for tree in range(len(arrInput[i])):
            if arrInput[i][tree] == highestTree:
                continue
            elif arrInput[i][tree] > highestTree:
                highestTree = arrInput[i][tree]
                toAdd = str(i) + ',' + str(tree)
                treeSets.add(toAdd)

    for i in range(len(arrInput)-1, -1, -1):
        if arrInput[i][98] >= 0:
            highestTree = arrInput[i][98]
            toAdd = str(i) + ',98'
            treeSets.add(toAdd)
        else:
            highestTree = 0

        for tree in range(len(arrInput[i])-1, -1, -1):
            if arrInput[i][tree] == highestTree:
                continue
            elif arrInput[i][tree] > highestTree:
                highestTree = arrInput[i][tree]
                toAdd = str(i) + ',' + str(tree)
                treeSets.add(toAdd)

    return treeSets

def columnCheck(arrInput):
    treeSets = set()
    for i in range(len(arrInput)):
        if arrInput[i][0] >= 0:
            highestTree = arrInput[i][0]
            toAdd = '0,' + str(i)
            treeSets.add(toAdd)
        else:
            highestTree = 0

        for tree in range(len(arrInput[i])):
            if arrInput[i][tree] == highestTree:
                continue
            elif arrInput[i][tree] > highestTree:
                highestTree = arrInput[i][tree]
                toAdd = str(tree) + ',' + str(i) 
                treeSets.add(toAdd)

    for i in range(len(arrInput)-1, -1, -1):
        if arrInput[i][98] >= 0:
            highestTree = arrInput[i][98]
            toAdd = '98,' + str(i)
            treeSets.add(toAdd)
        else:
            highestTree = 0

        for tree in range(len(arrInput[i])-1, -1, -1):
            if arrInput[i][tree] == highestTree:
                continue
            elif arrInput[i][tree] > highestTree:
                highestTree = arrInput[i][tree]
                toAdd = str(tree) + ',' + str(i)
                treeSets.add(toAdd)

    return treeSets

totalSet = rowCheck(array2d) | columnCheck(array2d2)
print(len(totalSet))