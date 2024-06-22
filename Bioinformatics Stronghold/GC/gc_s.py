'''
https://rosalind.info/problems/gc/

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.
'''
#list is a list that contains each line of the input file
list = []
#headers is a list that contains every header of the input file
headers = []

file = open('rosalind_gc.txt')
for line in file: 
    #the solution requires the header to not have a > at the beginning
    element = line.rstrip('\n').replace('>', '')
    list.append(element)
    if 'R' in element:
        headers.append(element)
file.close()

'''
each sequence is split among multiple lines in the .txt, 
so I had to join all of the lines for each sequence
to do that i joined every line of the file into one big string
but replacing each header with the letter d
this string will have each sequence preceded by the letter d: dAGCdTTG ecc.
I then split this big string using .split('d')
and then "popped" the first element (which is '')
'''
sequences = ''
for i in list:
    if 'R' in i:
        sequences += 'd'
    else:
        sequences += i
sequences = sequences.split('d')
sequences.pop(0)

#dict where key:value = GCcontent:Header
dict = {}
for i in range(len(headers)):
    dict[((sequences[i].count('G') + sequences[i].count('C')) / len(sequences[i])) * 100] = headers[i]

max = 0
for key in dict:
    if key > max:
        max = key

output = open('rosalind_gc_solution.txt', 'w')
output.write(dict[max] + '\n' + str(max))
output.close()
