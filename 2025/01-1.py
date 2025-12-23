def moveDial(currentDial, direction, nPositions):
    if direction == 'L':
        return (currentDial + 100-(nPositions%100))%100
    else:
        return (currentDial + (nPositions%100))%100

def getPassword(instructions):
    currentDial = 50
    counter = 0
    for direction, nPositions in instructions:
        currentDial = moveDial(currentDial, direction, nPositions)
        if currentDial == 0:
            counter += 1

    return counter

def parseInstructions(inputText):
    return ((line[0], int(line[1:])) for line in inputText.splitlines())

if __name__ == "__main__":
    with open('01.in', 'r') as f:
        inputText = f.read()

    print(getPassword(parseInstructions(inputText)))
