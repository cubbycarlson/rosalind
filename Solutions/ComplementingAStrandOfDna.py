def complement(dna):
    complements = {"A": "T", "C": "G", "G": "C", "T": "A"}
    strand = ''
    for nucleotide in reversed(dna):
        strand += complements[nucleotide]
    return strand

#
# def complement(dna):
#     return dna.replace('A', 't').replace('C', 'g').replace('G', 'c').replace('T', 'a').upper()[::-1]
