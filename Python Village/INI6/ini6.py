file = open('rosalind_ini6.txt')
contents = file.read().rstrip('\n')
file.close()

contents_as_list = contents.split(' ')

words = {}

#when this loop "reencounters" the same word more than once
#the key that corresponds to that word get its value updated with the same 
#value each time
#example contents_as_list = ['hi', 'bye', 'hi']
#the first time the loop encounters hi it gets added to the dictionary
#and is assigned the value 2
#the second time that the llop gets to hi the value of the
#key 'hi' gets updated to the same number (2)

for word in contents_as_list:
    words[word] = contents_as_list.count(word)

output = open('rosalind_ini6_solution.txt', 'w')
for key, value in words.items():
    output.write(key + ' ' + str(value) + '\n')