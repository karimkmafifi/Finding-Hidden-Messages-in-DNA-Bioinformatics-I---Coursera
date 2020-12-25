def skewDiagram(genome):
    
    skewDiagramLst = [0]
    for nuc in genome:
        if nuc == 'G':
            skewDiagramLst.append(skewDiagramLst[-1]+1)
        elif nuc == 'C':
            skewDiagramLst.append(skewDiagramLst[-1]-1)
        else:
            skewDiagramLst.append(skewDiagramLst[-1])
    
    skewDiagramStr=''
    for val in skewDiagramLst:
        if len(skewDiagramStr) == 0:
            skewDiagramStr += str(val)
        else:
            skewDiagramStr += ' ' + str(val)
    return skewDiagramStr

def minSkew(genome):
    skewDiagramLst = [0]
    for nuc in genome:
        if nuc == 'G':
            skewDiagramLst.append(skewDiagramLst[-1]+1)
        elif nuc == 'C':
            skewDiagramLst.append(skewDiagramLst[-1]-1)
        else:
            skewDiagramLst.append(skewDiagramLst[-1])
    
    minSkewVal = min(skewDiagramLst)
    minSkewIndices = [i for i, x in enumerate(skewDiagramLst) if x == minSkewVal]
    
    minSkewStr=''
    for val in minSkewIndices:
        if len(minSkewStr) == 0:
            minSkewStr += str(val)
        else:
            minSkewStr += ' ' + str(val)
    return minSkewStr

#print(minSkew('CATTCCAGTACTTCGATGATGGCGTGAAGA'))
#f = open("C:/Users/karim.afifi/Desktop/Bioinformatics Specialization/Finding Hidden Messages in DNA (Bioinformatics I)/Week 2/dataset_7_6.txt", "r")
#genome_seq = f.read()
#print(minSkew(genome_seq))