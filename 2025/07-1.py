def advanceBeam(rowIndex, map):
    assert rowIndex > 0
    
    count = 0
    for k in range(len(map[rowIndex])):
        match (map[rowIndex-1][k], map[rowIndex][k]):
            case ('|', '.'):
                map[rowIndex][k] = '|'
            case ('|', '^'):
                map[rowIndex][k-1], map[rowIndex][k+1] = '|', '|'
                count += 1

    return count

def teleport(map):
    res = 0

    for row in range(1, len(map)):
        res += advanceBeam(row, map)
    
    return res

def setInitialMap(rawMap):
    for col in range(len(rawMap[0])):
        if rawMap[0][col] == 'S':
            rawMap[0][col] = '|'
    
    return rawMap

if __name__ == '__main__':
    with open('07.in', 'r') as f:
        inputText = f.read()
    
    rawMap = [list(row) for row in inputText.splitlines()]
    map = setInitialMap(rawMap)

    print(teleport(map))
