from functools import reduce

def ingredientsInRange(ingredientList, left, right):
    left = max(left, ingredientList[0])
    right = min(right, ingredientList[-1])

    if left > right:
        return set([])

    _, leftLimitIndex = indexFind(ingredientList, left, 0, len(ingredientList))
    rightLimitIndex, _ = indexFind(ingredientList, right, 0, len(ingredientList))

    res = set(ingredientList[i] for i in range(leftLimitIndex, rightLimitIndex+1))
    
    return res

def indexFind(list, value, leftLimitIndex, rightLimitIndex):
    middle = (leftLimitIndex + rightLimitIndex) // 2

    if leftLimitIndex + 1 == rightLimitIndex:
        return leftLimitIndex, rightLimitIndex

    if value < list[middle]:
        return indexFind(list, value, leftLimitIndex, middle)
    elif list[middle] == value:
        return middle, middle
    else: # value > list[middle]
        return indexFind(list, value, middle, rightLimitIndex)

def availableIngredients(ingredientList, rangeList):
    return reduce(
        lambda acc, cur: acc | cur,
        map(
            lambda range: ingredientsInRange(ingredientList, *range),
            rangeList
        ), 
        set([])
    )

def parseRange(line):
    limits = line.split('-')
    return int(limits[0]), int(limits[1])

if __name__ == '__main__':
    with open('05.in', 'r') as f:
        inputText = f.read()
    
    ranges, ingredients = inputText.split('\n\n')
    ranges = (parseRange(line) for line in ranges.splitlines())

    ingredients = sorted([int(line) for line in ingredients.splitlines()])

    print(len(availableIngredients(ingredients, ranges)))
