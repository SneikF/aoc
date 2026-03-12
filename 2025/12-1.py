def canTheyFit(grid, presents):
    if len(presents) == 0:
        return True
    print(presents)
    for i in range(len(presents)):
        present = presents[i]
        for position in whereToPut(present, grid):
            presents.pop(i)
            for version in versions(present):
                insert(version, position, grid)
                if canTheyFit(grid, presents):
                    return True
                remove(version, position, grid)
            presents.insert(i, present)
    
    return False

def whereToPut(present, grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if itFits((y,x), present, grid):
                yield (y,x)

def itFits(position, present, grid):
    y0, x0 = position
    for y in range(len(present)):
        for x in range(len(present[y])):
            try:
                if not (present[y][x] and not grid[y + y0][x + x0]):
                    return False
            except: continue

    return True

def insert(present, position, grid):
    y0, x0 = position
    for y in range(len(present)):
        for x in range(len(present[y])):
            if present[y][x]:
                grid[y + y0][x + x0] = 1

def remove(present, position, grid):
    y0, x0 = position
    for y in range(len(present)):
        for x in range(len(present[y])):
            if present[y][x]:
                grid[y + y0][x + x0] = 0

def parsePresent(presentText):
    return [
        [1 if char == "#" else 0 for char in line]
        for line in presentText.splitlines()[1:]
    ]

def parseProblems(problemsText, presents):
    for line in problemsText.splitlines():
        items = line.split(': ')
        width, length = tuple(map(int, items[0].split('x')))
        presentAmountList = list(map(int, items[1].split()))

        presentList = []
        for index, amount in enumerate(presentAmountList):
            presentList += [presents[index]]*amount
        
        yield ([[0]*width]*length, presentList)

def parse(inputText):
    items = inputText.split('\n\n')

    presents = list(map(parsePresent, items[:-1]))
    problems = items[-1]

    return parseProblems(problems, presents)

if __name__ == "__main__":
    with open("12.in") as f:
        inputText = f.read()

    print(sum(1 if canTheyFit(*problem) else 0 for problem in parse(inputText)))
