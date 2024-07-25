file = open('rosalind_cons.txt')
list = []
for line in file:
    list.append(line.rstrip('\n'))
file.close()

sequences = ''
for i in list:
    if 'R' in i:
        sequences += 'd'
    else:
        sequences += i
sequences = sequences.split('d')
sequences.pop(0)

A = ['A:']
C = ['C:']
G = ['G:']
T = ['T:']

for i in range (len(sequences[0])):
    A.append(0)
    C.append(0)
    G.append(0)
    T.append(0)

for seq in sequences:
    for position in range (1, len(sequences[0]) + 1):
        if seq[position - 1] == 'A':
            A[position] += 1
        elif seq[position - 1] == 'C':
            C[position] += 1
        elif seq[position - 1] == 'G':
            G[position] += 1
        elif seq[position - 1] == 'T':
            T[position] += 1

bases = [A, C, G, T]

cons = ''
for position in range (1, len(sequences[0]) + 1):
    max = 0
    char = ''
    for base in bases:
        if base[position] > max:
            max = base[position]
            char = base[0][0]
        base[position] = str(base[position])
    cons += char

output = open('rosalind_cons_solution.txt', 'w')
output.write(cons + "\n")
output.write(" ".join(A) + "\n")
output.write(" ".join(C) + "\n")
output.write(" ".join(G) + "\n")
output.write(" ".join(T))