from disjoint_set import DisjointSet
getAllPairs  = __import__("08-1").getAllPairs
distance  = __import__("08-1").distance

def createDecoration(sortedClosestPairs, allPoints):
    set = DisjointSet.from_iterable(allPoints)

    for point1, point2 in sortedClosestPairs:
        set.union(point1, point2)
        if len(list(set.itersets())) == 1:
            return point1[0] * point2[0]

if __name__ == '__main__':
    with open('08.in', 'r') as f:
        inputText = f.read()
    
    allPoints = [tuple(int(num) for num in line.split(',')) for line in inputText.splitlines()]

    allPairs = getAllPairs(allPoints)
    sortedClosestPairs = sorted(allPairs, key=distance)

    decoration = createDecoration(sortedClosestPairs, allPoints)

    print(decoration)
