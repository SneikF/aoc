from functools import reduce

def parseLights(text):
    text = text[1:-1]

    lights = 0
    for i in range(len(text)):
        if text[i] == '#':
            lights |= 1 << (len(text) - i - 1)
    
    return lights, len(text)

def parseButton(text, nLights):
    text = text[1:-1]
    indexes = map(int, text.split(','))
    
    return reduce(
        lambda acc, index: acc | (1 << (nLights - index - 1)),
        indexes,
        0
    )

def parse(text):
    items = text.split()
    lights, nLights = parseLights(items[0])
    buttons = [parseButton(line, nLights) for line in items[1:-1]]

    return lights, buttons

def subsets(set):
    for i in range(2 ** len(set)):
        yield [set[j] for j in range(len(set)) if i & (1 << j) != 0]

def lightProduced(buttons):
    return reduce(lambda x, y: x ^ y, buttons, 0)

if __name__ == '__main__':
    with open('10.in', 'r') as f:
        inputText = f.read()

    cases = (parse(line) for line in inputText.splitlines())
    answers = (min(
        len(sequence) for sequence in subsets(buttons) 
        if lightProduced(sequence) == lights
    ) for lights, buttons in cases)

    print(sum(answers))
