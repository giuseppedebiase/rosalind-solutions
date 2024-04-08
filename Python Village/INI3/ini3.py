'''
https://rosalind.info/problems/ini3/

Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
'''
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
