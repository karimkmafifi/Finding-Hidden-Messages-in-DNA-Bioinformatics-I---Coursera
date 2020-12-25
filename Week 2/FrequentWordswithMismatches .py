from itertools import product

def hammingDistance(str1, str2):
    hamDist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamDist += 1
    return hamDist

def approximatePatternCount(pattern, text, d):
    count = 0
    for i in range(len(text)-len(pattern)+1):
        newPattern = text[i:i+len(pattern)]
        if hammingDistance(pattern, newPattern) <= d:
            count += 1
    return count

def generatePatterns(k):
    bases = ['A', 'C', 'G', 'T']
    bases_comb = [''.join(base) for base in product(bases, repeat = k)]
    return bases_comb

def frequentWordsMismatches(text, k, d):
    pattCounts = []
    diffPattLst = generatePatterns(k)
    for pattern in diffPattLst:
        pattCounts.append(approximatePatternCount(pattern, text, d))
    maxCount = max(pattCounts)
    allFreqPatt = []
    for i in range(len(pattCounts)):
        if pattCounts[i] == maxCount:
            allFreqPatt.append(diffPattLst[i])
    allFreqPatt = list(set(allFreqPatt))
    allFreqPattStr = ''
    for pattern in allFreqPatt:
        if len(allFreqPattStr) == 0:
            allFreqPattStr += pattern
        else:
            allFreqPattStr += ' ' + pattern
    return allFreqPattStr
    
#print(frequentWordsMismatches('GTCAGCGAGCGACAGTCCGGCGATCCGGTCATCCGCAGCAGGTCATCCGGCGAGTCATCCGTCCGTGTTCCGCAGGTCAGTCACAGGCGATCCGCAGTGTTCCGCAGGTCACAGCAGTGTGTCAGTCAGCGATCCGGCGATCCGGCGAGCGACAGTGTTGTTGTTGTGTCAGCGATCCGGTCAGTCAGTCAGTCAGTCAGTCAGCGACAGGCGATCCGGTCAGTCATGTTCCGGCGAGCGATCCGTGTTGTGTCATCCGTGTGCGATGTTGTGCGACAGCAGGCGACAGGCGATGTTGTGCGATCCGTCCGGCGAGCGATCCGGCGATGTGTCAGTCATGT', 7, 2))