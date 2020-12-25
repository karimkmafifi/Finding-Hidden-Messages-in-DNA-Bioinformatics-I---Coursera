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

def reverseComplement(dnaSeq):
    eq_nuc = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    dnaSeqRev = ''
    for i in range(len(dnaSeq)-1, -1, -1):
        dnaSeqRev += eq_nuc[dnaSeq[i]]
    return dnaSeqRev

def generatePatterns(k):
    bases = ['A', 'C', 'G', 'T']
    basesComb = [''.join(base) for base in product(bases, repeat = k)]
    basesCombFinal = []
    for patt in basesComb:
        basesCombFinal.append([patt, reverseComplement(patt)])
    return basesCombFinal

def frequentWordsMismatchesComp(text, k, d):
    pattCounts = []
    diffPattLst = generatePatterns(k)
    for pattern in diffPattLst:
        count1 = approximatePatternCount(pattern[0], text, d)
        count2 = approximatePatternCount(pattern[1], text, d)
        pattCounts.append(count1 + count2)
    maxCount = max(pattCounts)
    allFreqPatt = []
    for i in range(len(pattCounts)):
        if pattCounts[i] == maxCount:
            allFreqPatt.append(diffPattLst[i][0])
    allFreqPatt = list(set(allFreqPatt))
    allFreqPattStr = ''
    for pattern in allFreqPatt:
        if len(allFreqPattStr) == 0:
            allFreqPattStr += pattern
        else:
            allFreqPattStr += ' ' + pattern
    return allFreqPattStr
    
#print(frequentWordsMismatchesComp('TGCCCCCTGCCCTGCTGCGCACCATGCTGCGTCCATGCGTGTGTGCAGTTGCGCACCAGTCCACCGCATGCGTGCACCTGCCCAGCACCGTCCCCCCAGTGCAGTCCGCACCTGCCCCCAGTGTCCATGCGCACCAGTTGCGTGTCCGTCCACCCCACCGTTGCCCAGCACCGTCCACCAGCACCGCAGCAGCAGCAGTGTGTCCCCAGCAGTCCAGCAGCAGTTGCCCAGT', 6, 2))