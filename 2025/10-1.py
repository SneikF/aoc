def parseLights(line):
    lights = ''
    for i in range(1, len(line)):
        if line[i] == '.':
            lights += '0'
        elif line[i] == '#':
            lights += '1'
        else:
            break
    return int(lights, base=2), len(lights)

def parseButton(text, nLights):
    res = 0
    indexes = eval(text)
    if type(indexes) is int:
        indexes = [indexes]
    for index in indexes:
        res |= 1 << (nLights - index - 1)
    return res


def parse(line):    
    lights, nLights = parseLights(line)
    line = line[nLights+2:].split()
    buttons = map(lambda line: parseButton(line, nLights), line[:-1])
    return lights, list(buttons)

def subsets(set):
    for i in range(2 ** len(set)):
        res = []
        for j in range(len(set)):
            if i & (1 << j):
                res.append(set[j])
        yield res

def lightProduced(buttons):
    res = 0
    for button in buttons:
        res ^= button
    return res

if __name__ == '__main__':
    with open('10.in', 'r') as f:
        inputText = f.read()

    cases = (parse(line) for line in inputText.splitlines())
    answers = (min(len(buttons) for buttons in subsets(case[1]) if lightProduced(buttons)==case[0]) for case in cases)
    print(sum(answers))



