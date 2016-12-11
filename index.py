from Solutions.ComplementingAStrandOfDna import complement
data = open('input.txt').read()
output = open('output.txt', 'w')
output.write(complement(data))
output.close()
print(open('output.txt').read())
