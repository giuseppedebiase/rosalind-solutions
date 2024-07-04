'''
https://rosalind.info/problems/iprb/

Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k
individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate.
'''
file = open('rosalind_iprb.txt')
contents = file.read().rstrip('\n')
file.close()
contents_as_list = contents.split(' ')

#AA = homozygous dominant, Aa = heterozygous, aa = homozygous recessive
#Total probability = sum (probability that specimen A reproduces with specimen B) * probability that the offspring has a dominant allele

#List that contains the number of AA, Aa and aa
pop = []

for i in contents_as_list:
    pop.append(int(i))

#all possible couples, using the formula C = n*(n-1)/2
total_pop = pop[0] + pop[1] + pop[2]
total_couples = (total_pop)*(total_pop - 1) / 2

#Probability that specimen A meets (m, and reproduces) with specimen B for... 
#specimen from the same group
AAmAA = (pop[0] * (pop[0] - 1) / 2) / total_couples
AamAa = (pop[1] * (pop[1] - 1) / 2) / total_couples
#specimen from two different groups
AAmAa = pop[0] * pop[1] / total_couples
Aamaa = pop[1] * pop[2] / total_couples
AAmaa = pop[0] * pop[2] / total_couples
#(C = n*(n-1)/2 and drawings to figure out the formulas above, but they work)

#Probability that the offspring from specimenA x specimenB has a dominant allele
AAxAA = 1
AAxAa = 1
Aaxaa = 0.5
AAxaa = 1
AaxAa = 0.75
#no aaxaa since the probability is 0

#Probability on line 19 * probability on line 29
Tot_AA_AA = AAmAA * AAxAA
Tot_AA_Aa = AAmAa * AAxAa
Tot_Aa_aa = Aamaa * Aaxaa
Tot_AA_aa = AAmaa * AAxaa
Tot_Aa_Aa = AamAa * AaxAa

Total_probability = Tot_AA_AA + Tot_AA_Aa + Tot_Aa_aa + Tot_AA_aa + Tot_Aa_Aa
Total_probability = round(Total_probability, 5)

output = open('rosalind_iprb_solution.txt', 'w')
output.write(str(Total_probability))
output.close()
