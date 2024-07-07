'''
https://rosalind.info/problems/prot/

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
Return: The protein string encoded by s.
'''
import re

#I used regex to make the dict smaller (otherwise I would've had to create 61 key:value pairs)
codons = {
    'F' : r'UU(U|C)',
    'L' : r'(UU(A|G)|CU[UCAG])',
    'S' : r'(UC[UCAG]|AG(U|C))',
    'Y' : r'UA(U|C)',
    'C' : r'UG(U|C)',
    'W' : r'UGG',
    'P' : r'CC[UCAG]',
    'H' : r'CA(U|C)',
    'Q' : r'CA(A|G)',
    'R' : r'(CG[UCAG]|AG(A|G))',
    'I' : r'AU[UCA]',
    'M' : r'AUG',
    'T' : r'AC[UCAG]',
    'N' : r'AA(U|C)',
    'K' : r'AA(A|G)',
    'V' : r'GU[UCAG]',
    'A' : r'GC[UCAG]',
    'D' : r'GA(U|C)',
    'E' : r'GA(A|G)',
    'G' : r'GG[UCAG]'
}

def translation(c):
    for aa, codon in codons.items():
        found = re.finditer(codon, c)
        for match in found:
            return aa

file = open('rosalind_prot.txt')
DNA_seq = file.read().rstrip('\n')
file.close()

#values of the first and the third base of each codon (starting with the first one)
start_codon = 0
end_codon = 3

protein_sequence = ''
k = len(DNA_seq)

#The while loop stop when the value of end_codon exceeds the length of the DNA sequence
while end_codon <= k:
    codon = DNA_seq[start_codon:end_codon]
    print(codon)
    if codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
        #TAA, TAG and TGA are the stop codons
        break
    else:
        protein_sequence += (translation(codon))
        start_codon += 3
        end_codon += 3

print(protein_sequence)
output = open('rosalind_prot_solution.txt', 'w')
output.write(protein_sequence)
