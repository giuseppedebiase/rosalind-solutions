file = open('rosalind_dna.txt')
dna = file.read().rstrip('\n')
file.close()

A = dna.count('A')
C = dna.count('C')
G = dna.count('G')
T = dna.count('T')

result = str(A) + ' ' + str(C) + ' ' + str(G) + ' ' + str(T)

output = open('rosalind_dna_solution.txt', 'w')
output.write(result)
output.close()