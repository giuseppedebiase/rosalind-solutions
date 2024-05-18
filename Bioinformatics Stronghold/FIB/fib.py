'''
https://rosalind.info/problems/fib/

Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, 
every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''
file = open('rosalind_fib.txt')
contents = file.read()
file.close()
contents = contents.split(' ')

n = int(contents[0])
k = int(contents[1])

adults = 1 #adult pairs
total = 0 #total pairs (adult pairs + litter pairs)
litter = 0 #litter pairs
total_litters = litter * k #number of pairs produced each month

for i in range (1, n):
    tot = adults + total_litters * k
    total_litters = adults
    adults = tot

output = open('rosalind_fib_solution.txt', 'w')
output.write(str(tot))
output.close()
