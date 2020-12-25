def suffix(pattern):
    suffix = pattern[1:len(pattern)]
    return suffix

def hammingDistance(str1, str2):
    hamDist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamDist += 1
    return hamDist

def neighbors(pattern, d):
    if d == 0:
        return pattern
    if len(pattern) == 1:
        return ['A', 'C', 'G', 'T']
    neighborhood = []
    suffixNeighbors = neighbors(suffix(pattern), d)
    for patt in suffixNeighbors:
        if hammingDistance(suffix(pattern), patt) < d:
            for nuc in 'ATCG':
                neighborhood.append(nuc + patt)
        else:
            neighborhood.append(pattern[0] + patt)
    return neighborhood

#print(' '.join(neighbors('ACGAGGCCC', 2)))