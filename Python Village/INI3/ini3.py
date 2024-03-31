file = open('rosalind_ini3.txt')
contents = file.read()
file.close()

contents = contents.split('\n')

string = contents[0]
numbers = contents[1].split(' ')

a = int(numbers[0])
b = int(numbers[1]) + 1
c = int(numbers[2])
d = int(numbers[3]) + 1

final_string = string[a:b] + ' ' + string[c:d]

output = open('rosalind_ini3_solution.txt', 'w')
output.write(final_string)
output.close()