parse = __import__("11-1").parse
incidenceList = __import__("11-1").incidenceList
nPathsBetween = __import__("11-1").nPathsBetween

if __name__ == '__main__':
    with open('11.in', 'r') as f:
        inputText = f.read()
    
    graph = parse(inputText)
    inc = incidenceList(graph)
    table = {}

    def nPaths(origin, destination):
        return nPathsBetween(origin, destination, inc, table)

    values = [
        nPaths('svr', 'dac') * nPaths('dac', 'fft') * nPaths('fft', 'out'),
        nPaths('svr', 'fft') * nPaths('fft', 'dac') * nPaths('dac', 'out'),
    ]

    print(sum(values))
