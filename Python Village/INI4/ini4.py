'''
https://rosalind.info/problems/ini4/

Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
'''
file = open('rosalind_ini4.txt')
contents = file.read().rstrip('\n')
file.close()
numbers = contents.split(' ')
print(numbers)

a = int(numbers[0])
b = int(numbers[1])

total = 0

for i in range (a, b + 1):
    if i % 2 != 0:
        total += i

output = open('rosalind_ini4_solution.txt', 'w')
output.write(str(total))
output.close()
