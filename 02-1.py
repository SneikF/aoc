def isValid(strNum):
    if len(strNum) % 2 == 1:
        return True
    
    firstMid = strNum[:len(strNum) // 2]
    # print(firstMid)

    # print((int(firstMid) * (1 + 10 ** (len(firstMid)))), int(strNum))

    invalid = (int(firstMid) * (1 + 10 ** (len(firstMid)))) == int(strNum)

    return not invalid

assert isValid('15')
assert not isValid('1515')
assert not isValid('11121112')
assert not isValid('1212')

def sumOfInvalidsInRange(start, end):
    res = 0
    for i in range(start, end + 1):
        if not isValid(str(i)):
            res += i
    
    return res

def sumOfInvalidsInCollection(ranges):
    res = 0

    for start, end in ranges:
        res += sumOfInvalidsInRange(start, end)
    
    return res

def parseInput(inputText):
    ranges = map(lambda range: range.split('-'), inputText.split(','))
    return ((int(range[0]), int(range[1])) for range in ranges)

if __name__ == '__main__':
    with open('02.in') as f:
        inputText = f.read()
    
    print(sumOfInvalidsInCollection(parseInput(inputText)))
