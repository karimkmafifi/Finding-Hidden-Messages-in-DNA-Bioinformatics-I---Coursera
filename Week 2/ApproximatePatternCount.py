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

#print(approximatePatternCount('GGGGG', 'GTGCCTTTCGCACCAGCAAGTACCGTGGTAGCCCGTATGGGGGGGTACAGATCATTTGCCGCGAGTGACAGACCGCCCACGTAAGTGGCTCGAACCACCCGACGCGAGTAACTTCACGGGGGGGCTCATTAGGAGTTAGCCATAGCCGACACCTCAAAATCAGTGATTTCTTAGAACAGCCCCACACGGAGGCGCGCTTAAGTAATGGACGGGTAGGTCGCTGGACGTTAGCAATAGCTGGAGACTTTTAGTCTTCGCATAATATGCTACTAAGCGATTCACTTAAATTAGTAACTGGTCACGCAAAGATTGTGTCTTCTAATT', 2))