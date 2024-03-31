file = open('rosalind_ini2.txt')
contents = file.read().rstrip('\n')
file.close()

numbers = contents.split(' ')

a = int(numbers[0])
b = int(numbers[1])

hypotenuse = a**2 + b**2

output = open('rosalind_ini2_solution.txt', 'w')
output.write(str(hypotenuse))
output.close()
