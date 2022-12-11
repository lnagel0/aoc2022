from elves1stPart import *

input = open("input.txt", encoding="utf-8")

backpacks = []
groups = []
buffer = []
matchingFirstSecond = []
firstCounter = 0
secondCounter = 1
thirdCounter = 2
totalPriorities = 0

for line in input:
    line = line.rstrip()
    backpacks.append(line)

class Group:
    def __init__(self, number, first, second, third):
        self.number = number
        self.first = first
        self.second = second
        self.third = third
        self.sharedItem = ''

for i in range(100):
    groups.append(Group(i, backpacks[firstCounter], backpacks[secondCounter], backpacks[thirdCounter]))
    firstCounter += 3
    secondCounter += 3
    thirdCounter += 3

for i in range(100):
    buffer = []
    matchingFirstSecond = []
    # First, I compare the first with the second, and only then I proceed with the third elf.
    for char in groups[i].first:
        for char2 in groups[i].second:
            if char == char2:
                buffer.append(char)
                break
    for item in buffer:
        if item not in matchingFirstSecond:
            matchingFirstSecond.append(item)
    # Now, I look for a match in the third elf:
    for match in matchingFirstSecond:
        if match in groups[i].third:
            groups[i].sharedItem = match
    
for i in range(100):
    totalPriorities += eval(groups[i].sharedItem)

print('The total sum of priorities per group is ', totalPriorities)