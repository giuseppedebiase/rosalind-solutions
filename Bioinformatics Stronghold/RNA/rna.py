'''
https://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.
'''
file = open('rosalind_rna.txt')
dna = file.read()
file.close()

rna = dna.replace("T", "U")

output = open('rosalind_rna_solution.txt', 'w')
output.write(rna)
output.close()
