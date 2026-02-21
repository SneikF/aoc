def getAllPairs(elements):
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            yield elements[i], elements[j]

def area(a, b):
    width = abs(b[0] - a[0]) + 1
    height = abs(b[1]-a[1]) + 1
    return width * height

if __name__ == '__main__':
    with open('09.in', 'r') as f:
        inputText = f.read()
    
    allPoints = [tuple(int(num) for num in line.split(',')) for line in inputText.splitlines()]
    
    print(max(area(*pair) for pair in getAllPairs(allPoints)))
