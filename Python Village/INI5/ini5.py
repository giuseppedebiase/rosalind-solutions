'''
https://rosalind.info/problems/ini5/

Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
'''
file = open('rosalind_ini5.txt')
output = open('rosalind_ini5_solution.txt', 'a')

line_number = 1

for line in file:
    if line_number % 2 == 0:
        output.write(line)
    line_number += 1
