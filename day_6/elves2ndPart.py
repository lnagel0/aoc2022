input = open("input.txt", encoding="utf-8")

parsedInput = ''
bufferSet = []
counter = 0
counter2 = 0
score = 0


for line in input:
    parsedInput = line.rstrip()

for character in parsedInput:
    bufferSet.append(set())

    for character in parsedInput:
        
        if counter < 14:
            bufferSet[counter2].add(character)
        elif counter == 14:
            counter = 0
            break
        counter += 1

    if len(bufferSet[counter2]) == 14:
        break

    parsedInput = parsedInput[1:]

    counter2 += 1

score = 13 + len(bufferSet)
print(bufferSet, score)