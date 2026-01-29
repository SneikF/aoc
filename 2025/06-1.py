from math import prod

def solveProblem(numbers, operator):
    numbers = map(int, numbers)

    match operator:
        case '+':
            return sum(numbers)
        case '*':
            return prod(numbers)

def getTotal(problems):
    return sum(map(lambda problem: solveProblem(*problem), problems))

if __name__ == '__main__':
    with open('06.in', 'r') as f:
        inputText = f.read()
    
    data = [row.split() for row in inputText.splitlines()]

    numbers = zip(*data[:-1])
    operators = data[-1]

    problems = zip(numbers, operators)

    print(getTotal(problems))
