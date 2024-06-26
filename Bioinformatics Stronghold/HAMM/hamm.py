sequences = []

file = open('rosalind_hamm.txt')
for sequence in file:
    sequences.append(sequence.rstrip('\n'))
file.close()

hamm = 0

for i in range(len(sequences[0])):
    print(i)
    if sequences[0][i] != sequences[1][i]:
        hamm += 1

output = open('rosalind_hamm_solution.txt', 'w')
output.write(str(hamm))