# from Solutions.ComplementingAStrandOfDna import complement
# data = open('input.txt').read()
# output = open('output.txt', 'w')
# output.write(complement(data))
# output.close()
# print(open('output.txt').read())

# from Bio import SeqIO
#
# for record in SeqIO.parse('input.txt', 'fasta'):
#     print(record.id, len(record))
#

from Solutions.tools.codons import codons
print(codons)