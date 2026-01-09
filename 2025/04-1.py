def isReachable(y, x, plane):
    return nearbyPaperRolls(y, x, plane) < 4

def nearbyPaperRolls(y, x, plane):
    return sum(1 if plane[y][x] == '@' else 0 for y, x in neighbors(y, x, plane))

def insidePlane(y, x, plane):
    return y >= 0 and y < len(plane) and x >= 0 and x < len(plane[0])

def getDeltas(dims):
    if dims == 2:
        return [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    
    # TODO: general implementation

def neighbors(y, x, plane):
    deltas = getDeltas(2)
    return ((y+dy, x+dx) for dy, dx in deltas if insidePlane(y+dy, x+dx, plane))

def reachableRolls(plane):
    return [
        (y, x)
        for y in range(len(plane))
        for x in range(len(plane[0]))
        if plane[y][x] == '@' and isReachable(y, x, plane)
    ]

def nReachableRolls(plane):
    return sum(
        int(plane[y][x] == '@' and isReachable(y, x, plane))
        for y in range(len(plane))
        for x in range(len(plane[0]))
    )

if __name__ == "__main__":
    with open('04.in', 'r') as file:
        inputText = file.read()
    plane = inputText.splitlines()
    print(nReachableRolls(plane))
