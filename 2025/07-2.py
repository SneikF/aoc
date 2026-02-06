setInitialMap  = __import__("07-1").setInitialMap
teleport  = __import__("07-1").teleport
def nPathsInRow(rowIndex, map):
    newRow = map[rowIndex][:]
    for col in range(len(map[rowIndex])):
        if map[rowIndex][col] != '|':
            newRow[col] = 0
        else:
            newRow[col] = map[rowIndex-1][col]
            try:
                if map[rowIndex][col-1] == '^':
                    newRow[col] += map[rowIndex-1][col-1]
            except: pass
            try:
                if map[rowIndex][col+1] == '^':
                    newRow[col] += map[rowIndex-1][col+1]
            except: pass
    
    map[rowIndex] = newRow

def nPathsInMap(map):
    for rowIndex in range(1, len(map)):
        nPathsInRow(rowIndex, map)


if __name__ == '__main__':
    with open('07.in', 'r') as f:
        inputText = f.read()
    
    rawMap = [list(row) for row in inputText.splitlines()]
    map = setInitialMap(rawMap)
    teleport(map)
    map[0] = [1 if cell == '|' else 0 for cell in map[0]]
    nPathsInMap(map)

    print(sum(map[-1]))
