def parse(inputText):
    lines = inputText.splitlines()
    graph = {}

    for line in lines:
        nodes = line.split()
        origin = nodes[0][:-1]
        destinations = nodes[1:]
        graph[origin] = destinations
    
    graph['out'] = []

    return graph

def incidenceList(graph):
    return {node: [inc for inc in graph if node in graph[inc]] for node in graph}

def nPathsBetween(origin, destination, incidenceList, table):
    handle = f'{origin},{destination}'
    if handle in table:
        return table[handle]

    if origin == destination:
        res = 1
    else:
        res = sum(nPathsBetween(origin, dest, incidenceList, table) for dest in incidenceList[destination])
    
    table[handle] = res

    return res

if __name__ == '__main__':
    with open('11.in', 'r') as f:
        inputText = f.read()
    
    graph = parse(inputText)
    inc = incidenceList(graph)
    print(nPathsBetween('you', 'out', inc, {}))
