file = open('rosalind_ini5.txt')
output = open('rosalind_ini5_solution.txt', 'a')

line_number = 1

for line in file:
    if line_number % 2 == 0:
        output.write(line)
    line_number += 1