def canTheyFit(grid, presents):
    gridArea = len(grid) * len(grid[0])
    presentsMinArea = sum(sum(sum(line) for line in present) for present in presents)

    return presentsMinArea <= gridArea

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
        
        yield ([[0 for _ in range(width)] for _ in range(length)], presentList)

def parse(inputText):
    items = inputText.split('\n\n')

    presents = list(map(parsePresent, items[:-1]))
    problems = items[-1]

    return parseProblems(problems, presents)

if __name__ == "__main__":
    with open("12.in") as f:
        inputText = f.read()

    print(sum(1 if canTheyFit(*problem) else 0 for problem in parse(inputText)))
