from Bio import SeqIO
from Bio.SeqUtils import GC


def my_gc(string):
    count = 0
    for i in string:
        if i == 'C' or i == 'G':
            count += 1
    return round(count/len(string), 9) * 100

highest_percentage = 0
highest_id = ''
for record in SeqIO.parse('../input.txt', 'fasta'):
    current_percentage = GC(record.seq)
    if current_percentage > highest_percentage:
        highest_percentage = current_percentage
        highest_id = record.id
print(highest_id + '\n' + str(highest_percentage))