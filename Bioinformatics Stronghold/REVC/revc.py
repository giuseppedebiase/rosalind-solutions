file = open('rosalind_revc.txt')
dna = file.read()
file.close()

dna = dna.lower()
dna = dna.replace('a', 'T')
dna = dna.replace('t', 'A')
dna = dna.replace('c', 'G')
dna = dna.replace('g', 'C')

rev_dna = ''
base = -1
length = len(dna)
for i in range(length):
    rev_dna += dna[base]
    base -= 1

output = open('rosalind_revc_solution.txt', 'w')
output.write(rev_dna)
output.close()