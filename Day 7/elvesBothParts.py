from anytree import Node, RenderTree

input = open("input.txt", encoding="utf-8")

parsedInput = []
dirs = []
score = 0
dirSizes = {}
path = ['root']
score = 0
spaceUsed = 0

maxSpace = 70000000
reqFreeSpace = 30000000
dirToDeleteSpace = 0
freeSpace = 0

slash = '/'

for line in input:
    parsedInput.append(line.rstrip())

for line in parsedInput:

    if 'dir' in line:
        a, dirName = line.split()
    
        test = line.split()
    elif '$ cd' in line:
        if 'cd /' in line:
            path = ['root']
        elif 'cd ' in line and 'cd ..' not in line:
            a, b, pathName = line.split()
            path.append(pathName)
        elif 'cd ..' in line and path != ['root']:
            path.pop(len(path) - 1)
        elif 'cd ..' in line and path == ['root']:
            path = ['root']
    elif '$ ls' in line:
        pass
    else:
        pathiano = slash.join(path)
        path2 = path[:]
        size = line.split()

        for i in range(len(path)):
            pathiano = slash.join(path2)
            if pathiano in dirSizes:
                dirSizes[pathiano] += int(size[0])
            else:
                dirSizes[pathiano] = int(size[0])
            if len(path2) == 1:
                continue
            else:
                path2.pop(len(path2)-1)

for dir in dirSizes:
    if int(dirSizes[dir]) <= 100000:
        score += int(dirSizes[dir])

freeSpace = maxSpace - int(dirSizes['root'])

dirToDeleteSpace = reqFreeSpace - freeSpace

candidates = []

for dir in dirSizes:
    if int(dirSizes[dir]) > dirToDeleteSpace:
        print(dirSizes[dir])

string = '234925 gjsnzbtw.ncd'