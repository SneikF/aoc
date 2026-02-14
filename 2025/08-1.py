from disjoint_set import DisjointSet
from math import sqrt

def createDecoration(sortedClosestPairs, allPoints):
    set = DisjointSet.from_iterable(allPoints)

    for point1, point2 in sortedClosestPairs:
        set.union(point1, point2)

    return set

def getAnswer(decoration):
    sorted_sets = sorted(list(decoration.itersets()), key=len, reverse=True)

    return len(sorted_sets[0]) * len(sorted_sets[1]) * len(sorted_sets[2])

def cartesianProduct(setA, setB):
    return [(a, b) for a in setA for b in setB]

def getAllPairs(elements):
    res = []
    for i in range(len(elements)):
        for j in range(i+1, len(elements)):
            res.append((elements[i], elements[j]))
    
    return res

def distance(pair):
    point1, point2 = pair
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    dx, dy, dz = x1-x2, y1-y2, z1-z2

    return sqrt(dx*dx+dy*dy+dz*dz)

if __name__ == '__main__':
    with open('08.in', 'r') as f:
        inputText = f.read()
    
    allPoints = [tuple(int(num) for num in line.split(',')) for line in inputText.splitlines()]

    allPairs = getAllPairs(allPoints)
    sortedClosestPairs = sorted(allPairs, key=distance)[:1000]

    decoration = createDecoration(sortedClosestPairs, allPoints)

    print(getAnswer(decoration))