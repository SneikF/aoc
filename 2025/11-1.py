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

def dfs(graph):
    passedBy = {node: False for node in graph}
    nPathsFromYou = {node: set([]) for node in graph}
    nPathsFromYou['you'] = set([str(['you'])])

    stack = ['you']
    while len(stack) > 0:
        cur = stack.pop()
        passedBy[cur] = True

        for node in graph[cur]:
            nPathsFromYou[node] |= set([str(eval(path) + [node]) for path in nPathsFromYou[cur]])
            stack.append(node)
        


    return len(nPathsFromYou['out'])

if __name__ == '__main__':
    with open('11.in', 'r') as f:
        inputText = f.read()
    
    print(dfs(parse(inputText)))
