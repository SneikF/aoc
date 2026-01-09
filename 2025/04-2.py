reachableRolls = __import__("04-1").reachableRolls

def cleanPlane(plane, toBeCleaned):
    for y, x in toBeCleaned:
        plane[y][x] = '.'

def nCleanableRolls(plane):
    res = 0
    toBeCleaned = reachableRolls(plane)
    while len(toBeCleaned) > 0:
        res += len(toBeCleaned)
        cleanPlane(plane, toBeCleaned)
        toBeCleaned = reachableRolls(plane)
    return res

if __name__ == "__main__":
    with open('04.in', 'r') as file:
        inputText = file.read()
    plane = inputText.splitlines()
    for i in range(len(plane)):
        plane[i] = list(plane[i])
    print(nCleanableRolls(plane))

    for row in plane:
        print(''.join(row))
