def immediateNeighbors(pattern):
    diffNucDict = {'A': ['T', 'C', 'G'], 'T': ['A', 'C', 'G'], 'C': ['T', 'A', 'G'], 'G': ['T', 'C', 'A']}
    neighborhood = []
    patternLst = [nuc for nuc in pattern]
    for i in range(1, len(patternLst)):
        symbol = patternLst[i]
        diffNucs = diffNucDict[symbol]
        for nuc in diffNucs:
            neighbor = pattern.copy()
            neighbor[i] = nuc
            neighborStr = ''.join(neighbor)
            neighborhood.append(neighborStr)
    return neighborhood