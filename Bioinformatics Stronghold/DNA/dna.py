'''
https://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''
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
