import numpy as np

input = open("input.txt", encoding = "utf-8")

pairs = []
firstPair = []
secondPair = []
score = 0
secondPartScore = 0
test = [True, False, True, True]

for line in input:
    pairs.append(line.rstrip())

for pair in pairs:
    splittedPairs = pair.split(',')
    firstPair.append(splittedPairs[0])
    secondPair.append(splittedPairs[1])

for pair in range(1000): # <- Amount of lines to be evaluated from input should go here
    splittedFirstPair = firstPair[pair].split('-')
    splittedSecondPair = secondPair[pair].split('-')

    firstList = list(range(int(splittedFirstPair[0]), int(splittedFirstPair[1]) + 1))
    secondList = list(range(int(splittedSecondPair[0]), int(splittedSecondPair[1]) + 1))

    coincident = (np.isin(firstList, secondList)).tolist()
    coincident2 = (np.isin(secondList, firstList)).tolist()
   
    if False in coincident or False in coincident2:
        if True in coincident or True in coincident2:
            secondPartScore += 1

    if coincident == coincident2 and (False not in coincident or False not in coincident2):
        score += 1
        secondPartScore += 1
    else:
        if True in coincident2:
            score += 1
            if False in coincident2:
                score -= 1

        if True in coincident:
            score += 1
            if False in coincident:
                score -= 1

print(score, secondPartScore)