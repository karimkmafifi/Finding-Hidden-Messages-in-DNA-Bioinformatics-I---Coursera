def patternCount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

def frequentWords(text, k, t):
    frequentPatterns = []
    counts = []
    for i in range(0, len(text)-k):
        pattern = text[i:i+k]
        count = patternCount(text, pattern)
        counts.append(count)
    
    for i in range(0, len(text)-k):
        if counts[i] >= t:
            frequentPatterns.append(text[i:i+k])
    frequentPatterns = list(set(frequentPatterns))
    return frequentPatterns

def clumpFinding(genome, k, l, t):
    clumpPatterns = []
    for i in range(len(genome)-l):
        clump = genome[i:i+l]
        freqWordsFound = frequentWords(clump, k, t)
        clumpPatterns = clumpPatterns + freqWordsFound
    clumpPatterns = list(set(clumpPatterns))
    
    clumpPatternsStr = ''
    for val in clumpPatterns:
        if len(clumpPatternsStr) == 0:
            clumpPatternsStr += val
        else:
            clumpPatternsStr += ' ' + val
    return clumpPatternsStr

#print(clumpFinding('CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG', 3, 25, 3))
#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Finding Hidden Messages in DNA (Bioinformatics I)/Week 1/E_coli.txt", "r")
#genome_seq = f.read()
#print(clumpFinding(genome_seq, 9, 500, 3))