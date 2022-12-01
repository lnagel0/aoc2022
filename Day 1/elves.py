input = open("input.txt", encoding="utf8")

inputCookies = []
parsedCookies = []
elvesAmount = []

currentCalories = 0
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

elvesAmount.sort(reverse=True)

print("The elf with the highest calories is carrying a total of ", elvesAmount[0], " calories.")
print("The 2nd elf with the highest calories is carrying a total of ", elvesAmount[1], " calories.")
print("The 3rd elf with the highest calories is carrying a total of ", elvesAmount[2], " calories. \n")

print("In total, they're carrying ", elvesAmount[0] + elvesAmount[1] + elvesAmount[2], " calories.")