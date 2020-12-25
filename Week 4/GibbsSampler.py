import random
import numpy as np
from functools import reduce

def profileCalculateProbsKmers(text, k, profile):
    
    profileCols = []
    for j in range(len(profile[0])):
        col = []
        for i in range(len(profile)):
            col.append(profile[i][j])
        profileCols.append(col)

    allKmersProbs = []
    for i in range(len(text)-k+1):
        pattern = text[i:i+k]
        probabilities = []
        for j in range(len(pattern)):
            if pattern[j] == 'A':
                probabilities.append(profileCols[j][0])
            elif pattern[j] == 'C':
                probabilities.append(profileCols[j][1])
            elif pattern[j] == 'G':
                probabilities.append(profileCols[j][2])
            elif pattern[j] == 'T':
                probabilities.append(profileCols[j][3])
        prob = reduce((lambda x, y: x * y), probabilities)
        allKmersProbs.append(prob)
    return allKmersProbs

def createProfileMatrixPseudoCount(lstMotifs):
    probMatrix = {'A': [], 'C': [], 'G': [], 'T': []}
    for j in range(len(lstMotifs[0])):
        colNucs = []
        for i in range(len(lstMotifs)):
            colNucs.append(lstMotifs[i][j])
        ANucCount = colNucs.count('A')
        CNucCount = colNucs.count('C')
        GNucCount = colNucs.count('G')
        TNucCount = colNucs.count('T')
        ANucCount += 1
        CNucCount += 1
        GNucCount += 1
        TNucCount += 1
        NucCountSum = ANucCount + CNucCount + GNucCount + TNucCount
        ANucProb = ANucCount / NucCountSum
        CNucProb = CNucCount / NucCountSum
        GNucProb = GNucCount / NucCountSum
        TNucProb = TNucCount / NucCountSum
        probMatrix['A'].append(ANucProb)
        probMatrix['C'].append(CNucProb)
        probMatrix['G'].append(GNucProb)
        probMatrix['T'].append(TNucProb)
    return probMatrix

def hammingDistance(str1, str2):
    hamDist = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamDist += 1
    return hamDist

def getConsensus(motifs):
    consensus = ''
    for j in range(len(motifs[0])):
        col = []
        for i in range(len(motifs)):
            col.append(motifs[i][j])
        consensus += max(col, key = col.count)
    return consensus
    
def score(motifs):
    consensus = getConsensus(motifs)
    score = 0
    for motif in motifs:
        score += hammingDistance(consensus, motif)
    return score

def gibbsSampler(dna, k, t, n):
    motifs = []
    for seq in dna:
        startingIndex = random.randint(0,len(seq)-k-1)
        randPattern = seq[startingIndex:startingIndex+k]
        motifs.append(randPattern)
    
    bestMotifs = motifs
    bestMotifsScore = score(bestMotifs)
    for itr in range(n):
        i = random.randint(0, t-1)
        bestMotifsCopy = bestMotifs.copy()
        motifs = bestMotifs.copy()
        bestMotifsCopy.pop(i)
        
        profileMatrix = createProfileMatrixPseudoCount(bestMotifsCopy)
        profileMatrixEdited = []
        profileMatrixEdited.append(profileMatrix['A'])
        profileMatrixEdited.append(profileMatrix['C'])
        profileMatrixEdited.append(profileMatrix['G'])
        profileMatrixEdited.append(profileMatrix['T'])
        
        allKmersProbs = profileCalculateProbsKmers(dna[i], k, profileMatrixEdited)
        allKmersProbs = list(np.array(allKmersProbs) / sum(allKmersProbs))
        
        motifIndex = np.random.choice(a=len(dna[i])-k+1, p=allKmersProbs)
        motifi = dna[i][motifIndex:motifIndex+k]
        
        motifs[i] = motifi
        motifsScore = score(motifs)
        
        if motifsScore < bestMotifsScore:
            bestMotifs = motifs
            bestMotifsScore = motifsScore
            
    return [bestMotifs, bestMotifsScore]


#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Finding Hidden Messages in DNA (Bioinformatics I)/Week 4/dataset_163_4.txt", "r")
#data = f.readlines()
#f.close()
#k = 0
#t = 0
#n = 0
#dnaStrings = []
#for i in range(len(data)):
#    line = data[i]
#    lineEdit = line
#    if line[-1:] == '\n':
#        lineEdit = line[:-1]
#    if i == 0:
#        lstVals = lineEdit.split(' ')
#        k = int(lstVals[0])
#        t = int(lstVals[1])
#        n = int(lstVals[2])
#    else:
#        dnaStrings.append(lineEdit)

#minMotifs = []
#for i in range(20):
#    if i == 0:
#        minMotifs = gibbsSampler(dnaStrings, k, t, n)
#    else:
#        foundMotifs = gibbsSampler(dnaStrings, k, t, n)
#        if foundMotifs[1] < minMotifs[1]:
#            minMotifs = foundMotifs

#print('\n'.join(minMotifs[0]))
#print(minMotifs[1])