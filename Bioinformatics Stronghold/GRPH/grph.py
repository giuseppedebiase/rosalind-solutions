file = open('rosalind_grph.txt')

sequences = {}
#the input sequences are split among multiple lines, this for loop
#creates a dict where key = header (without '>') and value = sequence
for line in file:
    if '>' in line:
        sequences[line.replace('>', '').rstrip('\n')] = ''
    else:
        sequences[list(sequences)[-1]] += line.rstrip('\n')
file.close()

solution = ''
for header1, seq1 in sequences.items():
    for header2, seq2 in sequences.items():
        #directed loops are not allowed (but directed cicles are)
        if header1 != header2 and seq1[-3:] == seq2 [0:3]:
            solution += header1 + ' ' + header2 + '\n'

output = open('rosalind_grph_solution.txt', 'w')
output.write(solution)
output.close()