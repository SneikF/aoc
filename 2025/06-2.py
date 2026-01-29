getTotal = __import__("06-1").getTotal

def parseProblems(columns):
    currentOperator = '+'
    currentProblem = []

    for column in columns:
        column = list(column)

        if column[-1] != ' ':
            currentOperator = column[-1]
        
        if all(chr == ' ' for chr in column):
            yield currentProblem, currentOperator
            currentProblem = []
        else:
            currentProblem.append(int(''.join(column[:-1]).strip()))
    
    yield currentProblem, currentOperator

if __name__ == '__main__':
    with open('06.in', 'r') as f:
        inputText = f.read()
    
    data = inputText.splitlines()
    columns = zip(*data)

    print(getTotal(parseProblems(columns)))
