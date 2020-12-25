def patternCount(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

#num_of_occr = patternCount('GAGGGCTCGTTATGAGGGCTCACAAGGGCTCCCAGGGCTCTCAGGGCTCCTTTGAGGGCTCAGGGCTCTAAGGGCTCTAGGGCTCGCAGGGCTCAGTAGCCTCGAACATATGAGGGCTCCCCAGGGCTCGTGTCAGCGGAGGGGACAGGGCTCAACTAGGGCTCGAGGGCTCGGACCGCATTGCAGGGCTCCCATAGGGCTCAGGGCTCAGGGCTCACGGGAGGGCTCCAAGCAGGGCTCAGGGCTCAGGGCTCCTGCGCAAGGGCTCCAGGGCTCTAGGGCTCAGGGCTCGTAGTGAGGGCTCGAGGGCTCAGGGCTCGTAAGGGCTCAAGGGCTCGCAGGGCTCCGAGGGCTCTCAGGGCTCAGGGCTCAAGGGCTCAACCTCTCTTTTGGTAGGGCTCGAATCAGGGCTCATAGGGCTCCAAAGGGCTCAGGGCTCAAGGGCTCAAGGGCTCAGGGCTCTAGGGCTCGTTGCTAGGGCTCAGGGCTCTTAGTAGGGCTCAAGGGCTCCGTCAGGGCTCGAGGGCTCGATAGGGCTCAGGGCTCGAGAGGGCTCTAAAGCAGGGCTCAGGGCTCAGGGCTCCGGTAGGCAGGGCTCAGGGCTCAAGGGCTCAGGGCTCAAGGGCTCTAGGGCTCAAGGGCTCATAGGGCTCCTAAGTCAGGGCTCTCGAGGGCTCCCAGGGCTCAAGGGCTCTAGAAGGGCTCAGGGCTCAGGGCTCAGGGCTCTATTAGGGCTCCTAGGGCTCAGGGCTCGCAGGGCTCAGAATAAGGGCTCGTAGGGCTCAGGGCTCAGGGCTCAAGGGCTCCAGGGCTCCGAGCCAGGGCTCAGGGCTCAAGGGCTCAGGGCTCTTAGGGCTCCAAAATCTCTAGGGCTCACAAGGGCTCTCAGGGCTCAGGGCTCAGGGCTCAGGGCTCGCAGGGCTCGAAGGGCTCGAGGGCTCAGGGCTCCGAGCAGGGCTCTTAGGGCTCAGATAGGGCTCTAGGGCTCGAGGGCTCGAGGGCTCCGCAGAAAGGGCTCCAAGGCTGAGGGCTCAGGGCTCCT', 'AGGGCTCAG')
#print(num_of_occr)