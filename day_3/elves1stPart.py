input = open("input.txt", encoding="utf-8")

a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z = 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52

compartment1 = []
compartment2 = []
counter = 0
counter2 = 0
matchingItems = []
slicedMatching = []
prioritySum = 0

for line in input:
    line = line.rstrip()
    length = int(len(line) / 2)
    firstSliced = slice(length)
    secondSliced = slice(length, length*2)
    compartment1.append(line[firstSliced])
    compartment2.append(line[secondSliced])

for compartment in compartment1:
    compartment2data = compartment2[counter]
    counter += 1
    
    for i in range(len(compartment)):
        for data in compartment2data:
            if data == compartment[i]:
                matchingItems.append('')
                matchingItems[counter2] += data
                break
    counter2 += 1

slicerino = slice(1)
for item in matchingItems:
    if len(item) > 1:
        slicedMatching.append(item[slicerino])
    elif item == '':
        break
    else:
        slicedMatching.append(item)

for item in slicedMatching:
    prioritySum += eval(item)

print('The total sum of the priorities is', prioritySum, ' for the first part of the problem.')