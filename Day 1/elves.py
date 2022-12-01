input = open("input.txt", encoding="utf8")

inputCookies = []
parsedCookies = []
elvesAmount = []

currentCalories = 0
counter = 0
counter2 = 0

for line in input:
    inputCookies.append(line.rstrip())

for cookie in inputCookies:
    if cookie != '':
        parsedCookies += [int(cookie)]
    else:
        parsedCookies += [cookie]

for cookie in parsedCookies:
    if cookie != '':
        currentCalories += cookie
    elif cookie == '':
        elvesAmount.append(currentCalories)
        currentCalories = 0

for amount in elvesAmount:
    if amount > counter:
        counter = amount

for amount in elvesAmount:
    if amount != counter:
        counter2 += 1
    elif amount == counter:
        counter2 += 1
        break

print("The elf with the highest calories is the elf number ", counter2, " carrying a total of ", counter, " calories.")