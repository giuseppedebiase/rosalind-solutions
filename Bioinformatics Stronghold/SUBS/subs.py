'''
https://rosalind.info/problems/subs/

Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
'''
#no regex beacause it would've made solving the problem too easy
file = open('rosalind_subs.txt', 'r')
seq = file.readline().rstrip('\n')
motif = file.readline().rstrip('\n')
file.close()

positions = []
for i in range(len(seq) - len(motif)):
    if seq[i:i + len(motif)] == motif:
        positions.append(str(i + 1))

positions = (' ').join(positions)

output = open('rosalind_subs_solution.txt', 'w')
output.write(positions)
output.close()
