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

def getKmers(lstDNASeq, k, d):
    allKmers = []
    for seq in lstDNASeq:
        for i in range(len(seq)-k+1):
            pattern = seq[i:i+k]
            allKmers.append(pattern)
            allKmers = allKmers + neighbors(pattern, d)
    allKmers = list(set(allKmers))
    return allKmers

def motifEnumeration(lstDNASeq, k, d):
    patterns = []
    allKmers = getKmers(lstDNASeq, k, d)
    
    for kmer in allKmers:
        appearsInAll = True
        for seq in lstDNASeq:
            found = False
            for i in range(len(seq)-k+1):
                pattern = seq[i:i+k]
                if hammingDistance(kmer, pattern) <= d:
                    found = True
                    break
            if found == False:
                appearsInAll = False
                break
        if appearsInAll:
            patterns.append(kmer)
            
    return ' '.join(patterns)

#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Finding Hidden Messages in DNA (Bioinformatics I)/Week 3/dataset_156_8.txt", "r")
#data = f.readlines()
#k = 0
#d = 0
#lstDNAPatterns = []
#for i in range(len(data)):
#    line = data[i]
#    lineEdit = line
#    if line[-1:] == '\n':
#        lineEdit = line[:-1]
#    if i == 0:
#        k = int(lineEdit.split(' ')[0])
#        d = int(lineEdit.split(' ')[1])
#    else:
#        lstDNAPatterns.append(lineEdit)

#print(motifEnumeration(lstDNAPatterns, k, d))