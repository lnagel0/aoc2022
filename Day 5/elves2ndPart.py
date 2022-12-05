input = open("input.txt", encoding="utf-8")

stack1 = ['F', 'C', 'P', 'G', 'Q', 'R']
stack2 = ['W', 'T', 'C', 'P']
stack3 = ['B', 'H', 'P', 'M', 'C']
stack4 = ['L', 'T', 'Q', 'S', 'M', 'P', 'R']
stack5 = ['P', 'H', 'J', 'Z', 'V', 'G', 'N']
stack6 = ['D', 'P', 'J']
stack7 = ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R']
stack8 = ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J']
stack9 = ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']

instructions = []
removeBuffer = []

def moveCrate(amount, From, toWhere):
    destinedStack = eval('stack' + str(toWhere))
    currentStack = eval('stack' + str(From))
    
    for i in range(amount):
        removeBuffer.append(i+1)
    
    removeBuffer.reverse()
    currentStack.reverse()
    print(removeBuffer)
    for i in removeBuffer:
        destinedStack.append(currentStack.pop(i-1))
    
    currentStack.reverse()
        
for line in input:
    instructions.append(line.rstrip())

for instruction in instructions:
    splittedInstructions = instruction.split()
    
    amount = int(splittedInstructions[1])
    From = int(splittedInstructions[3])
    toWhere = int(splittedInstructions[5])

    moveCrate(amount, From, toWhere)

    removeBuffer = [] # Here I reset the buffer of the function. Probably there is another better way to do it.

print(stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9)