file = open('rosalind_fibd.txt')
contents = file.read()
file.close()
contents = contents.split(' ')

n = int(contents[0]) #months
m = int(contents[1]) #lifespan (months)
m_1 = m - 1

adults = 1
total_litters = 0

#stores the number of litters for each month
totlit_per_gen = {0: 1}

#starts from 2nd month (where there is only 1 adult pair and 0 litters)
for i in range (1, n):
    tot = adults + total_litters
    totlit_per_gen[i] = total_litters
    total_litters = adults
    #the litters born in a given month die after m months, so their number gets subtracted from the number of adults
    if i >= m_1:
        adults = tot - totlit_per_gen[i - m_1]
    else: 
        adults = tot

output = open('rosalind_fibd_solution.txt', 'w')
output.write(str(tot))
output.close()