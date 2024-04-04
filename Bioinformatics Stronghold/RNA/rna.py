file = open('rosalind_rna.txt')
dna = file.read()
file.close()

rna = dna.replace("T", "U")

output = open('rosalind_rna_solution.txt', 'w')
output.write(rna)
output.close()